from urllib.request import urlopen, Request
import ssl
from bs4 import BeautifulSoup
import re
from helpers import row_serializer

URL = 'https://live-tennis.eu/en/atp-live-ranking'

# opening website
req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
opened_url = urlopen(req, context=context)

# parsing website with BS
soup = BeautifulSoup(opened_url, 'html.parser')
player_rankings = soup.find(id='plyrRankings')
player_rows = player_rankings('tr', bgcolor=["#E7E7E7",'white'])
result = []
for row in player_rows:
    player_dict = row_serializer(row)
    result.append(player_dict)
print(result)

