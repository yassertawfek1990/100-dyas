import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")

tags =  soup.find_all(name="h3",class_ = "title")

titles_list = [title.getText() for title in tags]

# print(titles_list)
final_list = []
for i in titles_list:
    a = i.split()[0]
    b = " ".join(i.split()[1:])
    a = 101 - int(a[:-1])
    final_list.append(str(a) + ") " + b+"\n")

Final = titles_list[::-1]# to reverse a list
# for i in titles_list:
#     a = i.split()[0]
#     b = i.split()[1]
#     a = int(a[:-1])
print(final_list)
with open("movies.txt", "w",encoding="utf-8") as file:
    for movie in Final:
        file.write(f"{movie}\n ")
