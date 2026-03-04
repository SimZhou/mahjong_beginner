import os
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import urllib.parse
import time
import re

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

translator = GoogleTranslator(source='ja', target='zh-CN', proxies=proxies)

def translate_text(text):
    text = text.strip()
    if not text:
        return ""
    
    if re.match(r'^[\s\d\.\,\(\)\-\+\*\/]*$', text):
        return text

    protected = text
    for jp, zh in MAHJONG_DICT.items():
        protected = protected.replace(jp, zh)
    
    for attempt in range(5):
        try:
            translated = translator.translate(protected)
            if translated:
                return translated
        except Exception as e:
            print(f"Translation error ({attempt}): {e}")
            time.sleep(2 * (attempt + 1))
    return protected

def get_relative_prefix(md_path):
    depth = md_path.count('/')
    if depth == 0:
        return ""
    return "../" * depth

def download_image(img_url, img_filename):
    img_path = os.path.join('_source/docs', img_filename)
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

def process_page(name, href, md_path):
    url = urllib.parse.urljoin(BASE_URL, href)
    out_path = os.path.join('_source/docs', md_path)
    rel_prefix = get_relative_prefix(md_path)
    
    try:
        response = requests.get(url, proxies=proxies, timeout=15)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        main_contents = soup.find('div', id='main-contents')
        if not main_contents:
            print(f"Failed: No main-contents found in {href}")
            return False
            
        h1 = main_contents.find('h1')
        title = h1.text.strip() if h1 else name
        
        content_div = main_contents.find('div', class_='contents')
        if not content_div:
            print(f"Failed: No contents div found in {href}")
            return False
            
        for element in content_div.find_all(['script', 'noscript', 'hr']):
            element.decompose()
        for element in content_div.find_all('div', id='ad2'):
            element.decompose()
        for element in content_div.find_all('p', class_=['link-back2', 'link-next2']):
            element.decompose()

        md_content = f"# {translate_text(title)}\n\n"
        
        for element in content_div.children:
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
                            style = 'display:inline; vertical-align:middle; margin:0 1px;'
                            if width: style += f' width:{width}px;'
                            if height: style += f' height:{height}px;'
                            
                            rel_img_path = f"{rel_prefix}{img_filename}"
                            paragraph_md += f'<img src="{rel_img_path}" style="{style}" />'
                    elif child.name == 'span' and 'b' in child.get('class', []):
                        translated_span = translate_text(child.text)
                        paragraph_md += f"**{translated_span}**"
                    elif child.name == 'br':
                        paragraph_md += "\n"
                    elif child.name == 'a':
                        translated_a = translate_text(child.text)
                        paragraph_md += translated_a
                    elif isinstance(child, str):
                        translated_str = translate_text(child)
                        paragraph_md += translated_str
                    else:
                        text_val = child.text if hasattr(child, 'text') else str(child)
                        paragraph_md += translate_text(text_val)
                
                md_content += f"{paragraph_md}\n\n"
                
            elif element.name == 'h2':
                translated_h2 = translate_text(element.text.strip())
                md_content += f"## {translated_h2}\n\n"
                
            elif element.name == 'h3':
                translated_h3 = translate_text(element.text.strip())
                md_content += f"### {translated_h3}\n\n"
                
            elif element.name == 'ul':
                for li in element.find_all('li'):
                    translated_li = translate_text(li.text.strip())
                    md_content += f"- {translated_li}\n"
                md_content += "\n"
                
            elif element.name == 'img':
                img_src = element.get('src', '')
                img_filename = img_src.replace('../', '')
                if not img_filename.startswith('http'):
                    img_full_url = urllib.parse.urljoin(url, img_src)
                    download_image(img_full_url, img_filename)
                    rel_img_path = f"{rel_prefix}{img_filename}"
                    md_content += f'![]({rel_img_path})\n\n'
                    
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        print(f"Success: {href} -> {md_path}")
        return True
    except Exception as e:
        print(f"Error processing {href}: {e}")
        return False

def main():
    items = []
    with open('download_list.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                parts = line.strip().split('\t')
                if len(parts) == 3:
                    items.append(tuple(parts))
                    
    print(f"Starting to process {len(items)} pages sequentially...")
    
    # process only the non-index pages since we already customized index.md
    for name, href, md_path in items:
        process_page(name, href, md_path)
        time.sleep(1.5) # Sleep to avoid rate limiting
        
    print("Done generating markdown pages.")

if __name__ == '__main__':
    main()
