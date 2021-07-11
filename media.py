#! /usr/bin/python3
from bs4 import BeautifulSoup as bs
from PIL import Image
import os
import requests
import wget

def get_file(url, search): ## DL the page and save it
	r = requests.get(url)
	f = open(str(os.getcwd()+"/tmp/"+search), "w" )
	f.write(r.text)
	f.close()
	return r

class manga:
	def statut_scanfr(page): ## nombre chap et tome
		soup = bs(page.text, 'html.parser')
		statut = soup.find_all('span')
		statut = str(statut[4]).split()
		volume = soup.find_all('li')
		volume = str(volume[3])
		volume = volume.split()
		vol = volume.index('Volume')+1
		for i in range(len(statut)):
			if statut[i] == "cours</span>":
				stat = "ongoing"
			else:
				stat = "finish"
		print("Statut:", stat)
		print("nb of volume:", volume[vol])

	def dl_image(current_chap, dl_all, title, url):
		for page in chap:
			dir = os.makedirs(f"/home/{os.getlogin()}/Documents/{title}/{current_chap}")
			if dl_all == "Y" or dl_all == "y" or dl_all == 'Yes' or dl_all == 'YES' or dl_all == 'yes':
				dl_all = True
			else:
				dl_all = False

			r = Image.open(requests.get(url, stream=True).raw)
			r.save(f"{page}.jpg")

	def scanfr(title):
		url = 'https://www.scan-fr.cc/manga/'
		url_complete = url+title
		page = get_file(url_complete, title)
		manga.statut_scanfr(page)
		current_chap = input("Now select your chapter:")
		dl_all = input(f"do you want to Downloads all the chapter from the chapter {current_chap}: (Y/n)")
		manga.dl_image(current_chap, dl_all, title, url_complete)

class anime:
	def nyaa(title):
		url = 'https://nyaa.si/?f=0&c=0_0&q='
		url_complete = url+title
		#wget.download(url_complete, str(os.getcwd()+"/tmp/"+title))
		get_file(url_complete, title)