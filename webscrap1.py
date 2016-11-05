import requests
from bs4 import BeautifulSoup 

url = "http://www.nytimes.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text)
#print(soup)

g_data = soup.find_all(class_="story-heading")

for item in g_data:
	print(item.text.replace("\n" , " ").strip())