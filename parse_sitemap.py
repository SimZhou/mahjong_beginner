import os
from bs4 import BeautifulSoup
import yaml

with open('sitemap_raw.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

sitemap_ul = soup.find('ul', class_='sitemap')

nav = []
urls_to_download = []

if sitemap_ul:
    main_li = sitemap_ul.find('li')
    main_ul = main_li.find('ul', recursive=False)
    
    for category_li in main_ul.find_all('li', recursive=False):
        category_a = category_li.find('a', recursive=False)
        category_name = category_a.text.strip()
        
        pages_ul = category_li.find('ul', recursive=False)
        category_pages = []
        if pages_ul:
            for page_li in pages_ul.find_all('li', recursive=False):
                page_a = page_li.find('a', recursive=False)
                page_name = page_a.text.strip()
                href = page_a['href'].replace('../', '')
                
                if href.startswith('http'):
                    continue
                
                if not href.endswith('.html'):
                    continue
                
                md_path = href.replace('.html', '.md')
                category_pages.append({page_name: md_path})
                urls_to_download.append((page_name, href, md_path))
        
        if category_pages:
            nav.append({category_name: category_pages})

mkdocs_config = {
    'site_name': '麻将入门教程',
    'theme': {
        'name': 'material',
        'language': 'zh'
    },
    'nav': nav
}

with open('mkdocs.yml', 'w', encoding='utf-8') as f:
    yaml.dump(mkdocs_config, f, allow_unicode=True, sort_keys=False)

with open('download_list.txt', 'w', encoding='utf-8') as f:
    for name, href, md_path in urls_to_download:
        f.write(f"{name}\t{href}\t{md_path}\n")

print("Generated mkdocs.yml and download_list.txt")
