import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content , "html.parser")
    title = soup.find(class_ = "firstHeading").text

    print(f"{title} \nEnter Choice (y/n/e) : ")
    ans = input("").lower()
    
    if ans == "y":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        #break
    elif ans == "n":
        print("Try again!")
        continue
    elif ans == "e":
        exit(0)
