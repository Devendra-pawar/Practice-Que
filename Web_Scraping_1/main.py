


# code with harry


from xml.etree.ElementTree import Comment
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
url1= "https://www.geeksforgeeks.org/"
url2= "https://www.codewithharry.com/"

# Step 1: Get the HTML
r = requests.get(url2)
# print(r)
# print(r.url)
# print(r.status_code)
# print(r.content)


# ------------------------------------------------------------
# Step 2: Parse the HTML
soup = BeautifulSoup(r.content,"html.parser")
# print(soup)
# print(type(soup))
# print(soup.prettify())
# print(soup.get_text())

res = soup.title
# print(res)
# print(type(res))
# print(res.prettify())
# print(res.get_text())
# print(res.name)
# print(res.parent.name)
# print(res.string())
# print(type(res.string))

#----------------------------------------------------------
# Step 3: HTML Tree traversal

# Commonly used types of object:
# 1. Tag 
    #  print(type(res))
# 2. NavigableString
    #  print(type(res.string))
# 3. BeautifulSoup
    #  print(type(soup))
# 4. Comment
    # markup = "<p><!-- this is a comment --></p>"
    # soup2 = BeautifulSoup(markup)
    # print(soup2.p)
    # print(soup2.p.string)
    # print(type(soup2.p.string))



# Get the Title of th HTML page
# title = soup.title

# Get all the Paragraphs from the page
# paras = soup.find_all('p')
# print(paras)

# Get first element in te HTML page
# print(soup.find('p'))

# Get class of any element in te HTML page
# print(soup.find('p')['class'])

# Get all the elements with class lead
# print(soup.find_all("p",class_="lead"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())

# Get all the anchor tags from the page
# anchors = soup.find_all('a')
# print(anchors)

# Get all the links on the page:
# all_links = set()
# for link in anchors:
#     if(link.get('href') != 'a'):
#         linkText = "https://codewithharry.com" + link.get('href')
#         # all_links.add(link)
#         print(linkText)


navbarSupportedContent = soup.find(id='__next') # navbarSupportedContent
# .content - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for item in navbarSupportedContent.contents:
#     print(item)
# for item in navbarSupportedContent.stripped_string:
#     print(item)

# print(navbarSupportedContent.parent)
# print(navbarSupportedContent.parents)
# for item in navbarSupportedContent.parents:
#     print(item.name)

# item = soup.select('#loginModal')
# print(item)
# item = soup.select('.modal-footer')
# print(item)


# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------






