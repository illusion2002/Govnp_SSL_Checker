import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import logging

def get_links_from_url(url):
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')

        links = set()
        for a in soup.find_all('a', href=True):
            href = a['href'].strip()
            parsed = urlparse(href)
            domain = parsed.netloc or href
            if domain.endswith(".gov.np"):
                clean_domain = domain.replace("https://", "").replace("http://", "").strip("/").lower()
                links.add(clean_domain)

        return list(links)
    except Exception as e:
        logging.error(f"Failed to get links from {url}: {e}")
        return []
