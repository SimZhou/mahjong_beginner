#!/usr/bin/env node
/**
 * 预下载所有 HTML 页面到本地
 */
const fs = require('fs');
const axios = require('axios');
const path = require('path');

const BASE_URL = 'https://beginners.biz/';
const TEMP_DIR = '/tmp/temph';

async function downloadPage(url, outputPath) {
    try {
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            },
            timeout: 20000
        });

        fs.writeFileSync(outputPath, response.data, 'utf-8');
        console.log(`  ✓ ${path.basename(outputPath)}`);
        return true;
    } catch (err) {
        console.error(`  ✗ ${path.basename(outputPath)} - ${err.message}`);
        return false;
    }
}

async function main() {
    const args = process.argv.slice(2);
    const isTest = args.includes('--test');

    // 创建临时目录
    if (!fs.existsSync(TEMP_DIR)) {
        fs.mkdirSync(TEMP_DIR, { recursive: true });
    }

    // 读取下载列表
    const listContent = fs.readFileSync('download_list.txt', 'utf-8');
    const items = listContent
        .split('\n')
        .filter(line => line.trim())
        .map(line => line.split('\t'))
        .filter(parts => parts.length === 3);

    console.log(`共有 ${items.length} 个页面需要下载`);

    let processItems = items;
    if (isTest) {
        console.log('\n=== 测试模式：只下载第一个页面 ===');
        processItems = items.slice(0, 1);
    }

    let successCount = 0;
    let failCount = 0;

    for (let i = 0; i < processItems.length; i++) {
        const [name, href, mdPath] = processItems[i];
        const url = new URL(href, BASE_URL).href;
        const outputPath = path.join(TEMP_DIR, path.basename(href));

        console.log(`\n[${i + 1}/${processItems.length}] ${name}`);

        const success = await downloadPage(url, outputPath);
        if (success) {
            successCount++;
        } else {
            failCount++;
        }

        // 延迟避免请求过快
        await new Promise(resolve => setTimeout(resolve, 1500));
    }

    console.log('\n=== 下载完成 ===');
    console.log(`成功: ${successCount}`);
    console.log(`失败: ${failCount}`);
}

main().catch(console.error);
