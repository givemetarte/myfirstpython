import requests
from bs4 import BeautifulSoup

everytime_result = requests.get(
    "https://www.hankookilbo.com/News/Read/201911301819398871?did=NS&dtype=2&dtypecode=21383&prnewsid=")

everytime_soup = BeautifulSoup(everytime_result.text, "html.parser")

pagination = everytime_soup.find("article-header", {"class": "pagination"})

page = pagination.find_all('a')
print(page)
