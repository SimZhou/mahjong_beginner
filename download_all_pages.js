#!/usr/bin/env node
/**
 * 批量翻译工具 - 使用临时文件和脚本配合
 */
import fs from 'fs';
import path from 'path';
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);
const SOURCE_DIR = '_source/docs';
const DOWNLOAD_LIST = 'download_list.txt';
const BASE_URL = 'http://beginners.biz/';

function getRelativePrefix(mdPath) {
    const depth = (mdPath.match(/\//g) || []).length;
    if (depth === 0) return "";
    return "../".repeat(depth);
}

async function downloadPage(href, outputPath) {
    const url = new URL(href, BASE_URL).href;
    const curlCmd = `curl -s --connect-timeout 30 "${url}" -o "${outputPath}"`;

    try {
        await execAsync(curlCmd);

        // 检查文件是否有效
        const content = fs.readFileSync(outputPath, 'utf-8');
        if (content.includes('<!DOCTYPE') || content.includes('<html')) {
            return { success: true, size: content.length };
        }
        return { success: false, error: 'Invalid HTML' };
    } catch (err) {
        return { success: false, error: err.message };
    }
}

// 读取下载列表
const listContent = fs.readFileSync(DOWNLOAD_LIST, 'utf-8');
const items = listContent
    .split('\n')
    .filter(line => line.trim())
    .map(line => line.split('\t'))
    .filter(parts => parts.length === 3);

console.log(`共有 ${items.length} 个页面需要处理\n`);

// 输出待翻译列表（用于后续手动翻译）
const toTranslate = [];

for (let i = 0; i < items.length; i++) {
    const [name, href, mdPath] = items[i];
    const htmlPath = `/tmp/temph/${path.basename(href)}`;
    const fullHtmlPath = path.resolve(htmlPath);

    // 下载HTML
    console.log(`[${i + 1}/${items.length}] 下载: ${name}`);
    console.log(`  URL: ${new URL(href, BASE_URL).href}`);

    const result = await downloadPage(href, fullHtmlPath);

    if (result.success) {
        console.log(`  ✓ 下载成功 (${result.size} 字节)`);
        toTranslate.push({
            index: i + 1,
            name,
            href,
            mdPath,
            htmlPath: fullHtmlPath
        });
    } else {
        console.log(`  ✗ 下载失败: ${result.error}`);
    }

    // 延迟
    await new Promise(resolve => setTimeout(resolve, 1500));
}

// 保存待翻译列表
const listOutputPath = path.join(SOURCE_DIR, '.translation_list.json');
fs.writeFileSync(listOutputPath, JSON.stringify(toTranslate, null, 2), 'utf-8');

console.log(`\n=== 下载完成 ===`);
console.log(`成功: ${toTranslate.length}`);
console.log(`失败: ${items.length - toTranslate.length}`);
console.log(`\n待翻译列表已保存到: ${listOutputPath}`);
console.log(`\n接下来可以开始翻译任务...`);
