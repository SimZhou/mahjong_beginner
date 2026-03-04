#!/usr/bin/env python3
"""
重新翻译麻将网站 - 使用本地模型翻译能力
"""
import os
import sys
import requests
from bs4 import BeautifulSoup
import urllib.parse
import time
import re
import json

# 代理设置
proxies = {
    'http': 'http://127.0.0.1:10800',
    'https': 'http://127.0.0.1:10800'
}

BASE_URL = 'http://beginners.biz/'
OUTPUT_DIR = '_source/docs'

def get_relative_prefix(md_path):
    """计算相对路径前缀"""
    depth = md_path.count('/')
    if depth == 0:
        return ""
    return "../" * depth

def download_image(img_url, img_filename):
    """下载图片"""
    img_path = os.path.join(OUTPUT_DIR, img_filename)
    if os.path.exists(img_path):
        return True

    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    for attempt in range(3):
        try:
            r = requests.get(img_url, proxies=proxies, timeout=15)
            if r.status_code == 200:
                with open(img_path, 'wb') as f:
                    f.write(r.content)
                print(f"  [图片] 下载成功: {img_filename}")
                return True
        except Exception as e:
            print(f"  [图片] 下载失败 (尝试 {attempt + 1}/3): {e}")
            time.sleep(2)
    return False

def get_translation_from_original_text(jp_text, page_context=""):
    """
    准备翻译内容 - 这个函数将生成需要翻译的文本
    实际翻译将由用户手动完成或通过其他方式调用
    """
    return {
        'japanese': jp_text,
        'context': page_context
    }

def extract_page_content(html_content, href, md_path):
    """提取页面内容，不翻译，只准备待翻译内容"""
    soup = BeautifulSoup(html_content, 'html.parser')

    main_contents = soup.find('div', id='main-contents')
    if not main_contents:
        print(f"  [错误] 未找到 main-contents 区域")
        return None, None, None

    h1 = main_contents.find('h1')
    title = h1.text.strip() if h1 else "Unknown"

    content_div = main_contents.find('div', class_='contents')
    if not content_div:
        print(f"  [错误] 未找到 contents 区域")
        return None, None, None

    # 清理不需要的元素
    for element in content_div.find_all(['script', 'noscript', 'hr']):
        element.decompose()
    for element in content_div.find_all('div', id='ad2'):
        element.decompose()
    for element in content_div.find_all('p', class_=['link-back2', 'link-next2']):
        element.decompose()

    # 提取结构化内容
    elements = []

    for element in content_div.children:
        if element.name == 'p':
            # 处理段落
            p_content = {
                'type': 'p',
                'inline_elements': []
            }

            for child in element.children:
                if child.name == 'img':
                    img_src = child.get('src', '')
                    img_filename = img_src.replace('../', '')
                    if not img_filename.startswith('http'):
                        # 计算相对路径
                        rel_prefix = get_relative_prefix(md_path)
                        rel_img_path = f"{rel_prefix}{img_filename}"

                        # 下载图片
                        img_full_url = urllib.parse.urljoin(href, img_src)
                        download_image(img_full_url, img_filename)

                        p_content['inline_elements'].append({
                            'type': 'img',
                            'src': rel_img_path,
                            'style': child.get('style', ''),
                            'width': child.get('width', ''),
                            'height': child.get('height', '')
                        })
                elif child.name == 'span' and 'b' in child.get('class', []):
                    p_content['inline_elements'].append({
                        'type': 'strong',
                        'text': child.text.strip()
                    })
                elif child.name == 'br':
                    p_content['inline_elements'].append({
                        'type': 'br'
                    })
                elif child.name == 'a':
                    p_content['inline_elements'].append({
                        'type': 'a',
                        'text': child.text.strip()
                    })
                elif isinstance(child, str):
                    text = child.strip()
                    if text:
                        p_content['inline_elements'].append({
                            'type': 'text',
                            'text': text
                        })

            elements.append(p_content)

        elif element.name == 'h2':
            elements.append({
                'type': 'h2',
                'text': element.text.strip()
            })

        elif element.name == 'h3':
            elements.append({
                'type': 'h3',
                'text': element.text.strip()
            })

        elif element.name == 'ul':
            ul_content = {
                'type': 'ul',
                'items': []
            }
            for li in element.find_all('li'):
                ul_content['items'].append(li.text.strip())
            elements.append(ul_content)

        elif element.name == 'img':
            img_src = element.get('src', '')
            img_filename = img_src.replace('../', '')
            if not img_filename.startswith('http'):
                rel_prefix = get_relative_prefix(md_path)
                rel_img_path = f"{rel_prefix}{img_filename}"

                img_full_url = urllib.parse.urljoin(href, img_src)
                download_image(img_full_url, img_filename)

                elements.append({
                    'type': 'standalone_img',
                    'src': rel_img_path
                })

    return title, elements, soup

def process_single_page(name, href, md_path, translate_func=None):
    """处理单个页面"""
    url = urllib.parse.urljoin(BASE_URL, href)
    out_path = os.path.join(OUTPUT_DIR, md_path)
    out_json_path = out_path.replace('.md', '.json')

    print(f"\n处理: {name}")
    print(f"  URL: {url}")
    print(f"  输出: {md_path}")

    try:
        # 下载页面
        response = requests.get(url, proxies=proxies, timeout=20)
        response.encoding = 'utf-8'

        # 提取内容
        title, elements, soup = extract_page_content(response.text, url, md_path)
        if not title:
            print(f"  [失败] 无法提取内容")
            return False

        # 保存结构化内容到 JSON（待翻译）
        os.makedirs(os.path.dirname(out_json_path), exist_ok=True)
        with open(out_json_path, 'w', encoding='utf-8') as f:
            json.dump({
                'title': title,
                'elements': elements,
                'meta': {
                    'name': name,
                    'href': href,
                    'md_path': md_path
                }
            }, f, ensure_ascii=False, indent=2)

        print(f"  [成功] 已保存结构化数据到 {out_json_path}")

        # 如果有翻译函数，直接生成 Markdown
        if translate_func:
            md_content = translate_func(title, elements)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
            print(f"  [成功] 已生成 Markdown 到 {out_path}")

        return True

    except Exception as e:
        print(f"  [错误] 处理失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主函数"""
    # 读取下载列表
    items = []
    with open('download_list.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                parts = line.strip().split('\t')
                if len(parts) == 3:
                    items.append(tuple(parts))

    print(f"共有 {len(items)} 个页面需要处理")

    # 只处理第一个页面作为测试
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        print("\n=== 测试模式：只处理第一个页面 ===")
        items = items[:1]

    # 处理所有页面
    success_count = 0
    fail_count = 0

    for i, (name, href, md_path) in enumerate(items, 1):
        print(f"\n进度: {i}/{len(items)}")
        if process_single_page(name, href, md_path):
            success_count += 1
        else:
            fail_count += 1
        time.sleep(1)  # 避免请求过快

    print(f"\n=== 处理完成 ===")
    print(f"成功: {success_count}")
    print(f"失败: {fail_count}")

if __name__ == '__main__':
    main()
