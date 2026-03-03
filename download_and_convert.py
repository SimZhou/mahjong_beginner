import os
import re
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from deep_translator import GoogleTranslator
import urllib.parse
import time

NL = chr(10)
NNL = chr(10) + chr(10)

proxies = {
    'http': 'http://127.0.0.1:10800',
    'https': 'http://127.0.0.1:10800'
}

BASE_URL = 'http://beginners.biz/'

MAHJONG_DICT = {
    '麻雀': '麻将',
    'テンパイ': '听牌',
    'シャンテン': '向听',
    'メンツ': '面子',
    'ターツ': '搭子',
    '数牌': '数牌',
    '字牌': '字牌',
    '対子': '对子',
    'トイツ': '对子',
    '待ち': '听',
    '牌理': '牌理',
    '牌効率': '牌效',
    '有効牌': '有效牌',
    '浮き牌': '浮牌',
    'イーシャンテン': '一向听',
    'リャンシャンテン': '两向听',
    '手役': '役种',
    '役牌': '役牌',
    'ピンフ': '平和',
    'タンヤオ': '断幺九',
    '染め手': '染手',
    '三色': '三色',
    'ドラ': '宝牌',
    '赤牌': '红宝牌',
    '鳴き': '鸣牌',
    'ポン': '碰',
    'チー': '吃',
    'カン': '杠',
    '食いタン': '食断',
    'トイトイ': '对对和',
    'ホンイツ': '混一色',
    '後づけ': '后付',
    'リーチ': '立直',
    'ダマ': '默听',
    '守り': '防守',
    '守備': '防守',
    '安全牌': '安全牌',
    'スジ': '筋牌',
    'カベ': '壁牌',
    'ベタオリ': '弃和',
    'まわし打ち': '兜牌',
    '絞り': '扣牌',
    '状況判断': '局势判断',
    'オーラス': '最终局',
    '押し引き': '攻防判断',
    'ビギナーズラック': 'Beginners Luck'
}

def translate_text(text):
    if not text.strip():
        return ""
    protected = text
    for jp, zh in MAHJONG_DICT.items():
        protected = protected.replace(jp, zh)
    
    for attempt in range(3):
        try:
            translator = GoogleTranslator(source='ja', target='zh-CN', proxies=proxies)
            translated = translator.translate(protected)
            return translated if translated else protected
        except Exception as e:
            time.sleep(2)
    return protected

def download_image(img_url, img_filename):
    img_path = os.path.join('docs', img_filename)
    if os.path.exists(img_path):
        return
        
    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    for attempt in range(2):
        try:
            r = requests.get(img_url, proxies=proxies, timeout=10)
            if r.status_code == 200:
                with open(img_path, 'wb') as f:
                    f.write(r.content)
                break
        except Exception as e:
            time.sleep(1)

def process_page(item):
    name, href, md_path = item
    out_path = os.path.join('docs', md_path)
    
    # If the file exists and is not empty, skip. We already did ~80 pages.
    # We will only process failed/missing pages to save time!
    if os.path.exists(out_path) and os.path.getsize(out_path) > 100:
        # Check if the markdown file actually has translated content and not just title
        with open(out_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) > 2:
                return f"Skipped existing: {href}"
    
    url = urllib.parse.urljoin(BASE_URL, href)
    
    for attempt in range(3):
        try:
            response = requests.get(url, proxies=proxies, timeout=15)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            
            main_contents = soup.find('div', id='main-contents')
            if not main_contents:
                time.sleep(1)
                continue
                
            h1 = main_contents.find('h1')
            title = h1.text.strip() if h1 else name
            
            content_div = main_contents.find('div', class_='contents')
            if not content_div:
                time.sleep(1)
                continue
                
            for element in content_div.find_all(['script', 'noscript', 'hr']):
                element.decompose()
            for element in content_div.find_all('div', id='ad2'):
                element.decompose()
            for element in content_div.find_all('p', class_=['link-back2', 'link-next2']):
                element.decompose()

            md_content = f"# {translate_text(title)}{NNL}"
            
            for element in content_div.contents:
                if element.name == 'p':
                    paragraph_md = ""
                    for child in element.children:
                        if child.name == 'img':
                            img_src = child.get('src', '')
                            img_filename = img_src.replace('../', '')
                            if img_filename.startswith('http'):
                                pass
                            else:
                                img_full_url = urllib.parse.urljoin(url, img_src)
                                download_image(img_full_url, img_filename)
                                
                                width = child.get('width', '')
                                height = child.get('height', '')
                                style = ""
                                if 'hai/' in img_src:
                                    style = ' style="display:inline; vertical-align:middle; margin:0 1px;"'
                                    if width: style += f' width="{width}"'
                                    if height: style += f' height="{height}"'
                                
                                paragraph_md += f'<img src="/{img_filename}"{style}/>'
                        elif child.name == 'span' and 'b' in child.get('class', []):
                            paragraph_md += f"**{child.text}**"
                        elif child.name == 'br':
                            paragraph_md += NL
                        elif isinstance(child, str):
                            paragraph_md += child
                        else:
                            paragraph_md += child.text if hasattr(child, 'text') else str(child)
                    
                    translated_p = translate_text(paragraph_md)
                    md_content += f"{translated_p}{NNL}"
                    
                elif element.name == 'h2':
                    translated_h2 = translate_text(element.text.strip())
                    md_content += f"## {translated_h2}{NNL}"
                    
                elif element.name == 'h3':
                    translated_h3 = translate_text(element.text.strip())
                    md_content += f"### {translated_h3}{NNL}"
                    
                elif element.name == 'ul':
                    for li in element.find_all('li'):
                        translated_li = translate_text(li.text.strip())
                        md_content += f"- {translated_li}{NL}"
                    md_content += NL
                    
                elif element.name == 'img':
                    img_src = element.get('src', '')
                    img_filename = img_src.replace('../', '')
                    if not img_filename.startswith('http'):
                        img_full_url = urllib.parse.urljoin(url, img_src)
                        download_image(img_full_url, img_filename)
                        md_content += f'![]({img_filename}){NNL}'
                    
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
                
            return f"Success: {href} -> {md_path}"
        except Exception as e:
            time.sleep(2)
            
    return f"Failed: Completely failed on {href}"

def main():
    items = []
    with open('download_list.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                parts = line.strip().split('\t')
                if len(parts) == 3:
                    items.append(tuple(parts))
                    
    print(f"Starting to process {len(items)} pages...")
    
    items.insert(0, ('首页', 'index.html', 'index.md'))
    
    # Process sequentially to avoid dropping connections
    results = []
    for item in items:
        res = process_page(item)
        if "Failed" in res or "Success" in res:
            print(res)
             
    print("Done generating markdown pages.")

if __name__ == '__main__':
    main()
