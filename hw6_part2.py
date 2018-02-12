# 507/206 Homework 6 Part 2
import requests
from bs4 import BeautifulSoup


#### Part 2 ####
print('\n*********** PART 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Part 2 solution goes here
html = requests.get("https://www.michigandaily.com/").text
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())

most_read = soup.find(class_="view-id-most_read")
top_articles = most_read.find_all("a")

for article in top_articles:
    print(article.text)
