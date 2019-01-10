from urllib.request import urlopen, Request
import ssl
from bs4 import BeautifulSoup
import re

URL = 'https://live-tennis.eu/en/atp-live-ranking'

# opening website
req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
opened_url = urlopen(req, context=context)

# parsing website with BS
soup = BeautifulSoup(opened_url, 'html.parser')
print(soup)
