from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
content = response.text

soup = BeautifulSoup(content, "html.parser")

titles = soup.select(".titleline")
links = soup.select(".titleline a") # we select like in css first we get the class span tag with the class name .titleline then we get the a tag

title_list = []
links_list = []
for title_tag in titles:
    title = title_tag.getText()
    # print(title)
    title_list.append(title)

for i in range(len(links)):
    if i % 2 == 0:
        link = links[i].get("href")
        print(f" {i}: {link}")
        links_list.append(link)


scores_list = []
scores = soup.findAll(name="span" , class_ = "score")

for score_tag in scores:
    score = int(score_tag.getText().split()[0])
    # print(score)
    scores_list.append(score)

max_ind = scores_list.index(max(scores_list))

print(f"highest: {max_ind}")
best_title = title_list[max_ind]
best_link = links_list[max_ind]


print(len(links_list))

print(best_link)
print(best_title)