from urllib.request import urlopen, Request
import ssl
from bs4 import BeautifulSoup

URL = 'http://www.petertasschindler.me/'

# opening website
req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
opened_url = urlopen(req, context=context)

# parsing website with BS
soup = BeautifulSoup(opened_url, 'html.parser')


###################
### Tag element ###
###################

tag = soup.h1
tag
# <h1 style="color: white; padding:10px; border-radius: 10px; margin: 10px; text-shadow: 0px 0px 30px black; text-align: center;"><font size="10">Hi!</font></h1>

type(tag)
# <class 'bs4.element.Tag'>

tag.name
# h1

tag['style']
# color: white; padding:10px; border-radius: 10px; margin: 10px; text-shadow: 0px 0px 30px black; text-align: center;

tag.attrs # as string or list
# {'style': 'color: white; padding:10px; border-radius: 10px; margin: 10px; text-shadow: 0px 0px 30px black; text-align: center;'}

tag.get_attribute_list('style') # always as list
# ['color: white; padding:10px; border-radius: 10px; margin: 10px; text-shadow: 0px 0px 30px black; text-align: center;']


###############################
### NavigableString element ###
###############################

tag.string
# Hi!

type(tag.string)
# <class 'bs4.element.NavigableString'>

string = str(tag.string)
type(string)
# <class 'str'>


###########################
### Navigating the tree ###
###########################

soup.li # gets the first li tag
# <li class="wsite-menu-item-wrap" id="pg516701300478879176">
#     <a class="wsite-menu-item" href="about-me.html">
#         About Me
#     </a>
# </li>

soup.find_all('li') # gets the all li tags
# [
# <li class="wsite-menu-item-wrap" id="pg516701300478879176">
#     <a class="wsite-menu-item" href="about-me.html">
#         About Me
#     </a>
# </li>,
# <li class="wsite-menu-item-wrap" id="pg216966727224974482">
#     <a class="wsite-menu-item" href="education.html">
#         Education
#     </a>
# </li>,
# <li class="wsite-menu-item-wrap" id="pg584169040978597121">
#     <a class="wsite-menu-item" href="work-experience.html">
#         Work Experience
#     </a>
# </li>
# ]

