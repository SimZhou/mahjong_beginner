import requests

proxies = {
    'http': 'http://127.0.0.1:10800',
    'https': 'http://127.0.0.1:10800'
}

url = 'http://beginners.biz/sitemap/'
try:
    response = requests.get(url, proxies=proxies, timeout=10)
    response.encoding = 'utf-8' # the site seems to be Japanese, check charset
    with open('sitemap_raw.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print("Saved to sitemap_raw.html")
except Exception as e:
    print(f"Error: {e}")
