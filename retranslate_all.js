#!/usr/bin/env node
/**
 * 下载并重新翻译所有页面
 */
const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');
const axios = require('axios');
const { URL } = require('url');

const BASE_URL = 'http://beginners.biz/';
const SOURCE_DIR = '_source/docs';
const DOWNLOAD_LIST = 'download_list.txt';

function getRelativePrefix(mdPath) {
    const depth = (mdPath.match(/\//g) || []).length;
    if (depth === 0) return "";
    return "../".repeat(depth);
}

async function fetchPage(url, maxRetries = 3) {
    for (let attempt = 0; attempt < maxRetries; attempt++) {
        try {
            const response = await axios.get(url, {
                headers: {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                },
                timeout: 30000,
                responseType: 'arraybuffer'
            });

            if (response.status === 200) {
                return response.data.toString('utf-8');
            }
        } catch (err) {
            console.log(`    [尝试 ${attempt + 1}/${maxRetries} 失败: ${err.message}]`);
            await new Promise(resolve => setTimeout(resolve, 2000 * (attempt + 1)));
        }
    }
    return null;
}

function extractContent(html, pageUrl, mdPath) {
    const $ = cheerio.load(html);
    const mainContents = $('#main-contents');

    if (!mainContents.length) {
        console.log('    [警告] 未找到 main-contents 区域');
        return null;
    }

    const h1 = mainContents.find('h1').first();
    const title = h1.text().trim() || 'Unknown';

    const contentDiv = mainContents.find('.contents');
    if (!contentDiv.length) {
        console.log('    [警告] 未找到 contents 区域');
        return null;
    }

    // 清理不需要的元素
    contentDiv.find('script, noscript, hr').remove();
    contentDiv.find('#ad2').remove();
    contentDiv.find('.link-back2, .link-next2').remove();

    const elements = [];

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

                elements.push({
                    type: 'standalone_img',
                    src: relImgPath
                });
            }
        }
    });

    return { title, elements };
}

// 翻译函数 - 将日文翻译成中文
function translateText(text) {
    // 麻将术语映射
    const terms = {
        // 基本术语
        '麻雀': '麻将',
        '半荘': '半荘',
        '面子': '面子',
        '対子': '对子',
        'ターツ': '搭子',
        '听ち': '听牌',
        'テンパイ': '听牌',
        'シャンテン': '向听',
        'リーチ': '立直',
        'ダマ': '默听',
        'ポン': '碰',
        'チー': '吃',
        'カン': '杠',
        'ツモ': '自摸',
        'ロン': '荣和',
        '和': '和牌',
        '上がり': '和牌',
        'アガリ': '和牌',

        // 役名
        '役牌': '役牌',
        'ピンフ': '平和',
        'タンヤオ': '断幺九',
        '染め手': '染手',
        '三色': '三色',
        'トイトイ': '对对和',
        'ホンイツ': '混一色',
        '役満': '役满',
        'ドラ': '宝牌',
        '赤牌': '红宝牌',
        '食いタン': '食断',

        // 其他术语
        'ツキ': '运气',
        '流れ': '流势',
        'オカルト': '神秘学',
        '雀頭': '雀头',
        '有効牌': '有效牌',
        '浮き牌': '浮牌',
        '牌効率': '牌效',
        '牌理': '牌理',
        '守り': '防守',
        '守備': '防守',
        '安全牌': '安全牌',
        'スジ': '筋牌',
        'カベ': '壁牌',
        'ベタオリ': '弃和',
        '絞り': '扣牌',
    };

    // 简单替换
    for (const [jp, zh] of Object.entries(terms)) {
        text = text.replace(new RegExp(jp, 'g'), zh);
    }

    // 这里应该调用翻译API或模型，但由于我们在Node环境中，
    // 我们先保存日文原文，标记需要翻译
    return text;
}

function generateMarkdown(title, elements) {
    let md = `# ${title}\n\n`;

    for (const elem of elements) {
        if (elem.type === 'p') {
            for (const item of elem.inline_elements) {
                if (item.type === 'text') {
                    // 简单翻译
                    md += translateText(item.text) + ' ';
                } else if (item.type === 'strong') {
                    md += `**${translateText(item.text)}** `;
                } else if (item.type === 'br') {
                    md += '\n';
                } else if (item.type === 'img') {
                    const style = `display:inline; vertical-align:middle; margin:0 1px;`;
                    const width = item.width ? ` width="${item.width}"` : '';
                    const height = item.height ? ` height="${item.height}"` : '';
                    md += `<img src="${item.src}" style="${style}"${width}${height} />`;
                } else if (item.type === 'a') {
                    md += item.text;
                }
            }
            md += '\n\n';
        } else if (elem.type === 'h2') {
            md += `## ${translateText(elem.text)}\n\n`;
        } else if (elem.type === 'h3') {
            md += `### ${translateText(elem.text)}\n\n`;
        } else if (elem.type === 'ul') {
            for (const item of elem.items) {
                md += `- ${translateText(item)}\n`;
            }
            md += '\n';
        } else if (elem.type === 'standalone_img') {
            md += `<img src="${elem.src}" alt="示意图" />\n\n`;
        }
    }

    return md;
}

async function processSinglePage(name, href, mdPath) {
    const url = new URL(href, BASE_URL).href;
    const outPath = path.join(SOURCE_DIR, mdPath);

    console.log(`\n[${mdPath}] ${name}`);
    console.log(`  URL: ${url}`);

    try {
        // 下载页面
        console.log(`  [下载中...]`);
        const html = await fetchPage(url);

        if (!html) {
            console.log(`  [失败] 无法下载页面`);
            return false;
        }

        console.log(`  [下载成功] ${html.length} 字节`);

        // 提取内容
        const result = extractContent(html, url, mdPath);
        if (!result) {
            console.log(`  [失败] 无法提取内容`);
            return false;
        }

        const { title, elements } = result;
        console.log(`  [标题] ${title}`);
        console.log(`  [内容] ${elements.length} 个元素`);

        // 生成 Markdown（这里只做简单替换，完整翻译需要后续处理）
        const mdContent = generateMarkdown(title, elements);

        // 保存文件
        const dir = path.dirname(outPath);
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir, { recursive: true });
        }

        fs.writeFileSync(outPath, mdContent, 'utf-8');
        console.log(`  [成功] 已保存到 ${outPath}`);

        return true;
    } catch (err) {
        console.error(`  [错误] ${err.message}`);
        return false;
    }
}

async function main() {
    const args = process.argv.slice(2);
    const isTest = args.includes('--test');

    // 读取下载列表
    const listContent = fs.readFileSync(DOWNLOAD_LIST, 'utf-8');
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
        await new Promise(resolve => setTimeout(resolve, 2000));
    }

    console.log('\n=== 处理完成 ===');
    console.log(`成功: ${successCount}`);
    console.log(`失败: ${failCount}`);
}

main().catch(console.error);
