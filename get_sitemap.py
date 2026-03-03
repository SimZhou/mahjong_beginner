import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http://127.0.0.1:10800',
    'https': 'http://127.0.0.1:10800'
}

url = 'http://beginners.biz/sitemap/'
try:
    response = requests.get(url, proxies=proxies, timeout=10)
    response.encoding = 'utf-8' # the site seems to be Japanese, check charset
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Let's find all links in the main content area.
    # We might need to inspect the HTML structure, but usually sitemaps have a specific class or are just a list of links.
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith('http://beginners.biz/') or href.startswith('/'):
            if not href.startswith('http'):
                href = 'http://beginners.biz' + href
            links.append((a.text.strip(), href))
            
    with open('sitemap_links.txt', 'w', encoding='utf-8') as f:
        for text, link in links:
            f.write(f"{text}\t{link}\n")
    print(f"Found {len(links)} links. Saved to sitemap_links.txt")
except Exception as e:
    print(f"Error: {e}")
