#!/usr/bin/env node
/**
 * 从本地 HTML 文件提取内容并翻译
 */
const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');
const { URL } = require('url');

const BASE_URL = 'https://beginners.biz/';
const OUTPUT_DIR = '_source/docs';
const TEMP_HTML_DIR = '/tmp/temph';

function getRelativePrefix(mdPath) {
    const depth = (mdPath.match(/\//g) || []).length;
    if (depth === 0) return "";
    return "../".repeat(depth);
}

async function downloadImage(imgUrl, imgFilename) {
    const imgPath = path.join(OUTPUT_DIR, imgFilename);
    if (fs.existsSync(imgPath)) {
        return true;
    }

    const dir = path.dirname(imgPath);
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }

    try {
        const axios = require('axios');
        const response = await axios.get(imgUrl, {
            responseType: 'arraybuffer',
            timeout: 15000
        });

        if (response.status === 200) {
            fs.writeFileSync(imgPath, response.data);
            console.log(`  [图片] 下载成功: ${imgFilename}`);
            return true;
        }
        return false;
    } catch (err) {
        console.log(`  [图片] 跳过: ${imgFilename} (${err.message})`);
        return false;
    }
}

function extractContent(html, pageUrl, mdPath) {
    const $ = cheerio.load(html);
    const mainContents = $('#main-contents');

    if (!mainContents.length) {
        console.log('  [错误] 未找到 main-contents 区域');
        return null;
    }

    const h1 = mainContents.find('h1').first();
    const title = h1.text().trim() || 'Unknown';

    const contentDiv = mainContents.find('.contents');
    if (!contentDiv.length) {
        console.log('  [错误] 未找到 contents 区域');
        return null;
    }

    // 清理不需要的元素
    contentDiv.find('script, noscript, hr').remove();
    contentDiv.find('#ad2').remove();
    contentDiv.find('.link-back2, .link-next2').remove();

    const elements = [];

    // 处理 contents 下的所有子元素
    const children = contentDiv.children();
    children.each((_, elem) => {
        const tagName = elem.tagName;
        const $elem = $(elem);

        if (tagName === 'p') {
            const pContent = {
                type: 'p',
                inline_elements: []
            };

            $elem.contents().each((_, child) => {
                const $child = $(child);

                if (child.tagName === 'img') {
                    const imgSrc = $child.attr('src') || '';
                    let imgFilename = imgSrc.replace(/\.\.\//g, '');

                    if (!imgFilename.startsWith('http')) {
                        const relPrefix = getRelativePrefix(mdPath);
                        const relImgPath = `${relPrefix}${imgFilename}`;

                        // 异步下载图片（不阻塞）
                        const imgFullUrl = new URL(imgSrc, pageUrl).href;
                        downloadImage(imgFullUrl, imgFilename);

                        pContent.inline_elements.push({
                            type: 'img',
                            src: relImgPath,
                            style: $child.attr('style') || '',
                            width: $child.attr('width') || '',
                            height: $child.attr('height') || ''
                        });
                    }
                } else if (child.tagName === 'span' && $child.hasClass('b')) {
                    pContent.inline_elements.push({
                        type: 'strong',
                        text: $child.text().trim()
                    });
                } else if (child.tagName === 'br') {
                    pContent.inline_elements.push({ type: 'br' });
                } else if (child.tagName === 'a') {
                    pContent.inline_elements.push({
                        type: 'a',
                        text: $child.text().trim()
                    });
                } else if (child.type === 'text') {
                    const text = $(child).text().trim();
                    if (text) {
                        pContent.inline_elements.push({
                            type: 'text',
                            text: text
                        });
                    }
                }
            });

            if (pContent.inline_elements.length > 0) {
                elements.push(pContent);
            }
        } else if (tagName === 'h2') {
            elements.push({
                type: 'h2',
                text: $elem.text().trim()
            });
        } else if (tagName === 'h3') {
            elements.push({
                type: 'h3',
                text: $elem.text().trim()
            });
        } else if (tagName === 'ul') {
            const ulContent = {
                type: 'ul',
                items: []
            };
            $elem.find('li').each((_, li) => {
                ulContent.items.push($(li).text().trim());
            });
            if (ulContent.items.length > 0) {
                elements.push(ulContent);
            }
        } else if (tagName === 'img') {
            const imgSrc = $elem.attr('src') || '';
            let imgFilename = imgSrc.replace(/\.\.\//g, '');

            if (!imgFilename.startsWith('http')) {
                const relPrefix = getRelativePrefix(mdPath);
                const relImgPath = `${relPrefix}${imgFilename}`;

                const imgFullUrl = new URL(imgSrc, pageUrl).href;
                downloadImage(imgFullUrl, imgFilename);

                elements.push({
                    type: 'standalone_img',
                    src: relImgPath
                });
            }
        }
    });

    return { title, elements };
}

async function processSinglePage(name, href, mdPath) {
    const url = new URL(href, BASE_URL).href;
    const outJsonPath = path.join(OUTPUT_DIR, mdPath.replace('.md', '.json'));

    console.log(`\n处理: ${name}`);
    console.log(`  URL: ${url}`);
    console.log(`  输出: ${mdPath}`);

    try {
        // 先尝试从临时目录读取 HTML
        const tempHtmlPath = path.join(TEMP_HTML_DIR, path.basename(href));
        let html = null;

        if (fs.existsSync(tempHtmlPath)) {
            html = fs.readFileSync(tempHtmlPath, 'utf-8');
            console.log(`  [使用本地文件] ${tempHtmlPath}`);
        } else {
            // 尝试从网站下载
            try {
                const axios = require('axios');
                const response = await axios.get(url, {
                    headers: {
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                    },
                    timeout: 20000
                });
                html = response.data;
            } catch (err) {
                console.log(`  [警告] 无法从网站下载: ${err.message}`);
            }
        }

        if (!html) {
            console.log('  [失败] 无法获取 HTML 内容');
            return false;
        }

        const result = extractContent(html, url, mdPath);
        if (!result) {
            console.log('  [失败] 无法提取内容');
            return false;
        }

        const { title, elements } = result;

        // 保存结构化内容
        const dir = path.dirname(outJsonPath);
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir, { recursive: true });
        }

        const outputData = {
            title,
            elements,
            meta: {
                name,
                href,
                md_path: mdPath
            }
        };

        fs.writeFileSync(outJsonPath, JSON.stringify(outputData, null, 2), 'utf-8');
        console.log(`  [成功] 已保存到 ${outJsonPath}`);

        return true;
    } catch (err) {
        console.error(`  [错误] ${err.message}`);
        return false;
    }
}

async function main() {
    const args = process.argv.slice(2);
    const isTest = args.includes('--test');

    // 创建临时 HTML 目录
    if (!fs.existsSync(TEMP_HTML_DIR)) {
        fs.mkdirSync(TEMP_HTML_DIR, { recursive: true });
    }

    // 读取下载列表
    const listContent = fs.readFileSync('download_list.txt', 'utf-8');
    const items = listContent
        .split('\n')
        .filter(line => line.trim())
        .map(line => line.split('\t'))
        .filter(parts => parts.length === 3);

    console.log(`共有 ${items.length} 个页面需要处理`);

    let processItems = items;
    if (isTest) {
        console.log('\n=== 测试模式：只处理第一个页面 ===');
        processItems = items.slice(0, 1);
    }

    let successCount = 0;
    let failCount = 0;

    for (let i = 0; i < processItems.length; i++) {
        const [name, href, mdPath] = processItems[i];
        console.log(`\n进度: ${i + 1}/${processItems.length}`);

        const success = await processSinglePage(name, href, mdPath);
        if (success) {
            successCount++;
        } else {
            failCount++;
        }

        // 延迟避免请求过快
        await new Promise(resolve => setTimeout(resolve, 1000));
    }

    console.log('\n=== 处理完成 ===');
    console.log(`成功: ${successCount}`);
    console.log(`失败: ${failCount}`);
}

main().catch(console.error);
