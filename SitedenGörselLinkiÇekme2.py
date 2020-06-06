import requests
from bs4 import BeautifulSoup as bs
r = requests.get(
    "https://www.gettyimages.com/photos/harry-potter?family=editorial&page=2&phrase=harry%20potter&sort=mostpopular#license")
soup = bs(r.content, 'lxml')
soup.find_all("src"")
for photo in soup.find_all("src"):
    if photo != "None":
        print(photo.get("src"))
