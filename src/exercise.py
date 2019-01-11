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
player_rankings = soup.find(id='plyrRankings')
player_rows = player_rankings('tr', bgcolor=["#E7E7E7",'white'])
result = []
for row in player_rows[100:105]:
    ranking_tour = int(row.contents[0].text)
    full_name = row.contents[3].text.split(' ')
    first_name = full_name.pop(0)
    last_name = ' '.join(full_name)
    age = row.contents[4].text
    country = row.contents[5].contents[0]
    points_tour_live = row.contents[6].text
    ranking_tour_change = row.contents[7].text
    points_tour_change = row.contents[8].text
    current_tournament = row.contents[9].text.split(' ')
    current_tournament_round = current_tournament.pop(len(current_tournament)-1)
    current_tournament_name = ' '.join(current_tournament)
    in_tournament = False if len(current_tournament) == 1 else True
    previous_tournament = row.contents[10].text.split(' ')
    previous_tournament_round = previous_tournament.pop(len(previous_tournament)-1)
    previous_tournament_name = ' '.join(previous_tournament)
    current_tournament_name = current_tournament_name if len(current_tournament) > 1 else previous_tournament_name
    current_tournament_round = current_tournament_round if len(current_tournament) > 1 else previous_tournament_round
    points_tour_next = row.contents[12].text
    player_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "country": country,
        "age": age,
        "ranking_tour": ranking_tour,
        "ranking_tour_change": ranking_tour_change,
        "current_tournament_name": current_tournament_name,
        "current_tournament_round": current_tournament_round,
        "in_tournament": in_tournament,
        "points_tour_live": points_tour_live,
        "points_tour_next": points_tour_next,
        "points_tour_change": points_tour_change,
    }
    result.append(player_dict)
print(result)
