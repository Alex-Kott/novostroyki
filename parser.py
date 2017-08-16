import re
import requests as req
from bs4 import BeautifulSoup
import csv



builder_pages = 19
builders = []
# https://www.novostroyki.org/zastroyschiki/?search_text=&per_page=100&page=19
for k in range(1, builder_pages + 1):
	r = req.get("https://www.novostroyki.org/zastroyschiki/?search_text=&per_page=100&page={}".format(k))
	soup = BeautifulSoup(r.text, "lxml")
	links = soup.find_all(class_="co-link")
	for m in links:
		builders.append(m.a.contents[0])
	print("{} builder page".format(k))

with open("застройщики.csv", "w") as csvfile:
	writer = csv.writer(csvfile, dialect="excel", delimiter="\n")
	writer.writerow(builders)
csvfile.close()



building_pages = 140
buildings = []

for i in range(1, building_pages + 1):
	r = req.get("https://www.novostroyki.org/poisk_novostroek/?&page={}".format(i))
	soup = BeautifulSoup(r.text, "lxml")
	links = soup.find_all(class_="co-link")
	for j in links:
		buildings.append(j.a.contents[0])
	print("{} building page".format(i))

with open("новостройки.csv", "w") as csvfile:
	writer = csv.writer(csvfile, dialect="excel", delimiter="\n")
	writer.writerow(buildings)
csvfile.close()

