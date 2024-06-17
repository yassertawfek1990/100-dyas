from bs4 import BeautifulSoup
#import lxml

with open("website.html") as file:
    web = file.read()

soup = BeautifulSoup(web, "html.parser") #sometimes we need to uselxml.parser
print(soup.prettify())# print the content in a readable way
the_title = soup.title # that gets the title tag
print(the_title.name) #that prints the name of the tag

content = soup.a.string #that gets the string part of the first a tag
print(content)

all_a = soup.find_all(name="a") # to find all a tags

for tag in all_a: # we loop through them thn use getText to get the text
    print(tag.getText())
    print(tag.get("href")) # we use get to get a specific attribute of a tag

heading = soup.find("h1", id="name") # this will find first h1 tag with the id name then we can get text or whatever

section_heading = soup.find("h3", class_ ="heading") # this will find first h3 tag with the class heading then we can get text or whatever

name = soup.select_one("#name") # this will find the first tag with id = name

headings = soup.select(".heading") #this will find all tags with the class heading 

css_way = soup.select("p a") # this get all the tags with this selector anchor tag inside oaragraph tag same as we select in css