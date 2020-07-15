#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all('a'): #모든 a태그를 찾아라 그 a태그의 href를 찾아와서 프린트해라라는 의미
        print(anchor.get('href', '/'))