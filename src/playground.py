from urllib.request import urlopen, Request
import ssl
from bs4 import BeautifulSoup
import re

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


##########################
### Searching the tree ###
##########################

# Signature: find_all(name, attrs, recursive, string, limit, **kwargs)

soup.find_all('title') # string match
# [<title>Personal Website</title>]

for tag in soup.find_all(re.compile("t")): # regex match
    tag.name
# html
# title
# script
# meta
# style
# script
# script
# font
# font
# script
# script

soup.find_all(['title','script']) # list match
# [
#     <title>Personal Website</title>,
#     <script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-131840698-1"></script>,
# ]

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
soup.find_all(has_class_but_no_id) # function based match
# [
#     <a class="wsite-menu-item" href="darkroom.html">
#         Darkroom
#     </a>,
#     <a class="wsite-menu-item" href="contact.html">
#         Contact
#     </a>,
#     ...
# ]

soup.find_all(class_="wsite-menu-item",href="work-experience.html")
# [
#     <a class="wsite-menu-item" href="work-experience.html">
#         Work Experience
#     </a>,
#     <a class="wsite-menu-item" href="work-experience.html">
#         Work Experience
#     </a>
# ]

soup.find_all('a', string=re.compile('Contact'))
# [
#     <a class="wsite-menu-item" href="contact.html">
#         Contact
#     </a>,
#     <a class="wsite-menu-item" href="contact.html">
#         Contact
#     </a>
# ]

soup.find_all('a', string=re.compile('Contact'), limit=1)
# [
#     <a class="wsite-menu-item" href="contact.html">
#         Contact
#     </a>
# ]

soup('title') # no need for .find_all()
# [<title>Personal Website</title>]

# find_parents() => itterative version of .parents, works like find_all()
# find_parent() => itterative version of .parent, works like find()
# find_next_siblings() => itterative version of .next_siblings, works like find_all()
# find_next_sibling() => itterative version of .next_sibling, works like find()
# find_previous_siblings() => itterative version of .previous_siblings, works like find_all()
# find_previous_sibling() => itterative version of .previous_sibling, works like find()
# find_all_next() => itterative version of .next_elements, works like find_all()
# find_next() => itterative version of .next_element, works like find()
# find_all_previous() => itterative version of .previous_element, works like find_all()
# find_previous() => itterative version of .previous_element, works like find()
