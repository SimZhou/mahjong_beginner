#!/usr/bin/env node
/**
 * 修复所有 Markdown 文件中的图片路径
 * 将绝对路径（如 /images/xxx.gif）改为相对路径（如 ../images/xxx.gif）
 */
const fs = require('fs');
const path = require('path');

const SOURCE_DIR = '_source/docs';

function fixImagePathsInFile(filePath, depth) {
    const relPrefix = '../'.repeat(depth);

    try {
        let content = fs.readFileSync(filePath, 'utf-8');
        const originalContent = content;

        // 修复 /images/xxx.gif -> ../images/xxx.gif
        content = content.replace(/src="\/images\//g, `src="${relPrefix}images/`);

        // 修复 /hai/xxx.gif -> ../hai/xxx.gif
        content = content.replace(/src="\/hai\//g, `src="${relPrefix}hai/`);

        // 修复宽度="24"高度="34" -> width="24" height="34"
        content = content.replace(/宽度="(\d+)"高度="(\d+)"/g, 'width="$1" height="$2"');

        // 修复其他可能的问题
        // style 属性中的中文字符会导致问题，但先保留

        if (content !== originalContent) {
            fs.writeFileSync(filePath, content, 'utf-8');
            return { fixed: true, changes: '图片路径已修复' };
        }

        return { fixed: false };
    } catch (err) {
        console.error(`  [错误] ${filePath}: ${err.message}`);
        return { fixed: false, error: err.message };
    }
}

function fixAllMarkdownFiles(dir) {
    let fixedCount = 0;
    let totalCount = 0;
    let errorCount = 0;

    function scanDir(currentDir, depth) {
        const files = fs.readdirSync(currentDir);

        for (const file of files) {
            const fullPath = path.join(currentDir, file);
            const stat = fs.statSync(fullPath);

            if (stat.isDirectory()) {
                scanDir(fullPath, depth + 1);
            } else if (file.endsWith('.md')) {
                totalCount++;
                const relativePath = path.relative(SOURCE_DIR, fullPath);

                console.log(`\n[${totalCount}] ${relativePath} (depth: ${depth})`);
                const result = fixImagePathsInFile(fullPath, depth);

                if (result.fixed) {
                    console.log(`  ✓ ${result.changes}`);
                    fixedCount++;
                } else if (result.error) {
                    console.log(`  ✗ ${result.error}`);
                    errorCount++;
                } else {
                    console.log(`  - 无需修复`);
                }
            }
        }
    }

    scanDir(dir, 0);

    return { totalCount, fixedCount, errorCount };
}

function main() {
    console.log('开始修复 Markdown 文件中的图片路径...\n');

    if (!fs.existsSync(SOURCE_DIR)) {
        console.error(`错误：源目录不存在: ${SOURCE_DIR}`);
        process.exit(1);
    }

    const result = fixAllMarkdownFiles(SOURCE_DIR);

    console.log('\n=== 修复完成 ===');
    console.log(`总文件数: ${result.totalCount}`);
    console.log(`已修复: ${result.fixedCount}`);
    console.log(`错误: ${result.errorCount}`);
    console.log(`无需修复: ${result.totalCount - result.fixedCount - result.errorCount}`);
}

main();
