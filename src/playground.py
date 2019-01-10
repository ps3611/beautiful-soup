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

li_tag = soup.li
li_tag.contents # children of tag
# [
#     <a class="wsite-menu-item" href="about-me.html">
#         About Me
#     </a>
# ]

li_tag.children # to itterate over children
# <list_iterator object at 0x104ccb358>
children_list = list(li_tag.children) # same as .content
children_list
# [
#     <a class="wsite-menu-item" href="about-me.html">
#         About Me
#     </a>
# ]
len(children_list)
# 1

li_tag.descendants # to itterate over children
# <generator object Tag.descendants at 0x1026532a0>
descendant_list = list(li_tag.descendants)
descendant_list
# [
#     <a class="wsite-menu-item" href="about-me.html">
#         About Me
#     </a>,
#     About Me
# ]
len(descendant_list)
# 2

for string in li_tag:
    repr(string)
# '\n'
# <a class="wsite-menu-item" href="about-me.html">
#     About Me
# </a>
# '\n'

for string in li_tag.stripped_strings: # ignore whitespace
    repr(string)
# 'About Me'

a_tag = soup.a
a_tag
# <a class="wsite-menu-item" href="about-me.html">
#     About Me
# </a>

a_tag.parent
# <li class="wsite-menu-item-wrap" id="pg516701300478879176">
#     <a class="wsite-menu-item" href="about-me.html">
#         About Me
#     </a>
# </li>

for parent in a_tag.parents:
    if parent is None: #when you are at the top
        parent
    else:
        parent.name
# li
# ul
# div
# div
# div
# div
# body
# html
# [document]

li_tag.next_sibling
# <li class="wsite-menu-item-wrap" id="pg216966727224974482">
#     <a class="wsite-menu-item" href="education.html">
#         Education
#     </a>
# </li>

li_tag.previous_sibling.previous_sibling
# None

for sibling in li_tag.next_siblings:
    sibling
# <li class="wsite-menu-item-wrap" id="pg216966727224974482">
#     <a class="wsite-menu-item" href="education.html">
#         Education
#     </a>
# </li>
# <li class="wsite-menu-item-wrap" id="pg584169040978597121">
#     <a class="wsite-menu-item" href="work-experience.html">
#         Work Experience
#     </a>
# </li>

li_tag.next_element.next_element # the next element to the "li" tag is the "a" tag
# <a class="wsite-menu-item" href="about-me.html">
#     About Me
# </a>

