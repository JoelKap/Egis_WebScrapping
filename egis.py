
import requests
import json

from bs4 import BeautifulSoup

url = "https://github.com/egis/handbook/blob/master/Tech-Stack.md"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

links = soup.find_all('h2')
		#or link in links:
		#print((link[0].text))


programming 	= links[1].text
build 			= links[2].text
infrastructure	= links[3].text
monitor 		= links[4].text			

dataToPrint = ({"Technology":[{"build" : build, "infrastructure": infrastructure, "monitor": monitor}]})
data = json.dumps(dataToPrint["Technology"])
print(data)
