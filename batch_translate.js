import fs from 'fs';
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

// 待翻译的页面列表（kihon章节前10页）
const pages = [
    { name: '数牌与字牌', href: 'kihon/kihon05.html', md: 'kihon/kihon05.md' },
    { name: '对子（1）', href: 'kihon/kihon06.html', md: 'kihon/kihon06.md' },
    { name: '对子（2）', href: 'kihon/kihon07.html', md: 'kihon/kihon07.md' },
    { name: '基本形与复合形', href: 'kihon/kihon08.html', md: 'kihon/kihon08.md' },
    { name: '复合形（1）', href: 'kihon/kihon09.html', md: 'kihon/kihon09.md' },
    { name: '复合形（2）', href: 'kihon/kihon10.html', md: 'kihon/kihon10.md' },
    { name: '麻将的待（1）', href: 'kihon/kihon11.html', md: 'kihon/kihon11.md' },
    { name: '麻将的待（2）', href: 'kihon/kihon12.html', md: 'kihon/kihon12.md' },
];

console.log(`共有 ${pages.length} 个页面需要处理\n`);

async function downloadPage(href) {
    const htmlPath = `/tmp/temph/${path.basename(href)}`;
    const url = `http://beginners.biz/${href}`;
    
    try {
        await execAsync(`curl -s --connect-timeout 30 "${url}" -o "${htmlPath}"`);
        const content = fs.readFileSync(htmlPath, 'utf-8');
        if (content.includes('<!DOCTYPE') || content.includes('<html')) {
            return { success: true, path: htmlPath };
        }
        return { success: false };
    } catch (err) {
        return { success: false };
    }
}

import path from 'path';

async function main() {
    const results = [];
    
    for (let i = 0; i < pages.length; i++) {
        const page = pages[i];
        console.log(`[${i + 1}/${pages.length}] ${page.name}`);
        
        const result = await downloadPage(page.href);
        if (result.success) {
            console.log(`  ✓ 下载成功: ${result.path}`);
            results.push(page);
        } else {
            console.log(`  ✗ 下载失败`);
        }
        
        // 延迟
        await new Promise(resolve => setTimeout(resolve, 2000));
    }
    
    // 保存待翻译列表
    fs.writeFileSync('/tmp/temph/to_translate.json', JSON.stringify(results, null, 2), 'utf-8');
    
    console.log(`\n=== 下载完成 ===`);
    console.log(`成功: ${results.length}`);
    console.log(`待翻译列表已保存: /tmp/temph/to_translate.json`);
}

main().catch(console.error);
