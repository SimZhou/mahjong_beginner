#!/usr/bin/env node
/**
 * 改进翻译质量 - 修正常见的翻译错误
 */
const fs = require('fs');
const path = require('path');

const SOURCE_DIR = '_source/docs';

// 常见翻译错误映射表
const TRANSLATION_FIXES = {
    // 麻将术语修正
    '玛修': '麻将',
    '阿修': '麻将',
    '阿萨': '麻将',
    '阿育王': '麻将',
    '朝日': '麻将',
    'Asashi': '麻将',
    '大麻': '麻将',
    '大麻初学者通用课程': '麻将初学者通用课程',
    '大麻综合课程': '麻将综合课程',
    '麻雀头': '雀头',

    // 宝牌相关
    '宝藏瓷砖': '宝牌',
    '宝藏方块': '宝牌',
    '处理宝藏瓷砖': '处理宝牌',

    // 运气术语
    '运': '运气',
    '流量': '运气',
    '发推文': '运气好',
    '推文': '运气',

    // 麻将专业术语
    '半胜': '半荘',
    '半庄': '半荘',
    '面子': '面子',
    '对子': '对子',
    '搭子': '搭子',
    '听': '听牌',
    '听牌': '听牌',
    '向听': '向听',
    '立直': '立直',
    '碰': '碰',
    '吃': '吃',
    '杠': '杠',
    '自摸': '自摸',
    '和': '和牌',
    '胡': '和牌',
    'Tsumo': '自摸',
    'tsumo': '自摸',

    // 役名修正
    '平和': '平和',
    '断幺九': '断幺九',
    '对对和': '对对和',
    '混一色': '混一色',
    '大三元': '大三元',
    '役满': '役满',
    '宝牌': '宝牌',
    '红宝牌': '红宝牌',

    // 打牌术语
    '切': '切',
    '弃和': '弃和',
    '默听': '默听',
    '扣牌': '扣牌',
    '兜牌': '兜牌',

    // 其他术语
    '雀士': '雀士',
    '将军': '雀士',
    '末位': '末位',
    '末位确定': '末位确定',
    '末位确定（4位确定）': '末位确定（4位确定）',

    // 常见错误修正
    '阿加里': '和牌',
    'Lass': '末位',
    '阿萨将军': '雀士',
    'Konohansho': '亲家',
    'Masao': '麻将',

    // 特殊修正
    'I-P-co': '好型',
    '形状': '搭子',
};

// 需要保留不翻译的日文术语
const KEEP_JAPANESE = [
    '麻雀', // 麻将本身
    'ツキ', // 运气
    '流れ', // 流势
    'オカルト', // 神秘学
    'ビギナーズラック', // Beginners Luck
];

function fixTranslationInFile(filePath) {
    try {
        let content = fs.readFileSync(filePath, 'utf-8');
        const originalContent = content;

        // 应用翻译修正
        for (const [wrong, correct] of Object.entries(TRANSLATION_FIXES)) {
            const regex = new RegExp(wrong, 'g');
            content = content.replace(regex, correct);
        }

        // 修复一些常见的语法问题
        // "宽度="24"高度="34"" -> width="24" height="34"
        content = content.replace(/宽度="(\d+)"高度="(\d+)"/g, 'width="$1" height="$2"');

        // 修复一些明显的机器翻译错误
        content = content.replace(/"([^"]+)"/g, (match, p1) => {
            // 如果中文引号内容是日语，转换为日文引号
            if (p1.match(/[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]+/) && !p1.match(/[\u4E00-\u9FAF]+/)) {
                return `「${p1}」`;
            }
            return match;
        });

        // 修复多余的空格
        content = content.replace(/  +/g, ' ');

        // 修复标点符号问题
        content = content.replace(/，/g, '，');
        content = content.replace(/。/g, '。');
        content = content.replace(/、/g, '、');

        if (content !== originalContent) {
            fs.writeFileSync(filePath, content, 'utf-8');
            return { fixed: true };
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

    function scanDir(currentDir) {
        const files = fs.readdirSync(currentDir);

        for (const file of files) {
            const fullPath = path.join(currentDir, file);
            const stat = fs.statSync(fullPath);

            if (stat.isDirectory()) {
                scanDir(fullPath);
            } else if (file.endsWith('.md')) {
                totalCount++;
                const relativePath = path.relative(SOURCE_DIR, fullPath);

                console.log(`\n[${totalCount}] ${relativePath}`);
                const result = fixTranslationInFile(fullPath);

                if (result.fixed) {
                    console.log(`  ✓ 翻译已改进`);
                    fixedCount++;
                } else if (result.error) {
                    console.log(`  ✗ ${result.error}`);
                    errorCount++;
                } else {
                    console.log(`  - 无需改进`);
                }
            }
        }
    }

    scanDir(dir);

    return { totalCount, fixedCount, errorCount };
}

function main() {
    console.log('开始改进翻译质量...\n');
    console.log('修正的术语示例：');
    console.log('  玛修/阿修/朝日/阿育王 → 麻将');
    console.log('  流量/发推文 → 运气');
    console.log('  半胜/半庄 → 半荘');
    console.log('  将军 → 雀士');
    console.log('');

    if (!fs.existsSync(SOURCE_DIR)) {
        console.error(`错误：源目录不存在: ${SOURCE_DIR}`);
        process.exit(1);
    }

    const result = fixAllMarkdownFiles(SOURCE_DIR);

    console.log('\n=== 改进完成 ===');
    console.log(`总文件数: ${result.totalCount}`);
    console.log(`已改进: ${result.fixedCount}`);
    console.log(`错误: ${result.errorCount}`);
    console.log(`无需改进: ${result.totalCount - result.fixedCount - result.errorCount}`);
}

main();
