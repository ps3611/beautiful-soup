from urllib.request import urlopen, Request
import ssl

URL = 'https://live-tennis.eu/en/atp-live-ranking'

req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
opened_url = urlopen(req, context=context)
print(opened_url)
