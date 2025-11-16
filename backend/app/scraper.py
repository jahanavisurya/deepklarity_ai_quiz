from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

USER_AGENT = {'User-Agent': 'deepklarity-bot/0.1'}

def scrape_wikipedia(url: str) -> dict:
    parsed = urlparse(url)
    if 'wikipedia.org' not in parsed.netloc:
        raise ValueError('URL must be a wikipedia.org page')
    resp = requests.get(url, headers=USER_AGENT, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    title_tag = soup.find('h1', id='firstHeading')
    title = title_tag.get_text(strip=True) if title_tag else None
    content_div = soup.find('div', {'class':'mw-parser-output'})
    paragraphs = []
    sections = []
    full_text_parts = []
    if content_div:
        for child in content_div.children:
            if child.name == 'p':
                txt = child.get_text(strip=True)
                if txt:
                    paragraphs.append(txt)
                    full_text_parts.append(txt)
            if child.name in ['h2','h3']:
                heading = child.get_text(separator=' ', strip=True)
                sections.append(heading)
        full_text = '\n\n'.join(full_text_parts)
    else:
        full_text = ''
    summary = ' '.join(paragraphs[:3])
    return {'title': title, 'summary': summary, 'sections': sections, 'full_text': full_text}
