import requests
from bs4 import BeautifulSoup 

url = "http://www.nytimes.com/"
r = requests.get(url)

soup = BeautifulSoup(r.content)


g_data = soup.find_all("article", {"class": "story"})
for item in g_data:
	print(item.find_all("h2",{"class":"story-heading"})[0].text)