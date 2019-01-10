from urllib.request import urlopen, Request
import ssl
from bs4 import BeautifulSoup
import re

URL = 'https://live-tennis.eu/en/atp-live-ranking'

# opening website
req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
opened_url = urlopen(req, context=context)

# data needed
# {
#     "first_name",
#     "last_name",
#     "country",
#     "age",
#     "ranking_tour",
#     "ranking_tour_change",
#     "current_tournament_name",
#     "current_tournament_round",
#     "in_tournament",
#     "points_tour_live",
#     "points_tour_next",
#     "points_tour_change",
# }

# parsing website with BS
soup = BeautifulSoup(opened_url, 'html.parser')
player_rankings = soup.find(id='plyrRankings')
player_rows = player_rankings('tr', bgcolor=["#E7E7E7",'white'])
for row in player_rows:
    # row = player_rows[253]
    ranking_tour = int(row.contents[0].text)
    full_name = row.contents[3].text
    age = float(row.contents[4].text)
    country = row.contents[5].text
    points_tour_live = row.contents[6].text
    ranking_tour_change = row.contents[7].text
    points_tour_change = row.contents[8].text
    current_tournament_name = row.contents[9].text
    points_tour_next = row.contents[12].text
    player_dict = {
        "first_name": full_name,
        "last_name": full_name,
        "country": country,
        "age": age,
        "ranking_tour": ranking_tour,
        "ranking_tour_change": ranking_tour_change,
        "current_tournament_name": current_tournament_name,
        "current_tournament_round": current_tournament_name,
        "in_tournament": True,
        "points_tour_live": points_tour_live,
        "points_tour_next": points_tour_next,
        "points_tour_change": points_tour_change,
    }
    print(player_dict)
    print('----------')
