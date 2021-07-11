#! /usr/bin/python3
from bs4 import BeautifulSoup as bs
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
		statut = soup.prettify
		print(statut)

	def scanfr(title):
		url = 'https://www.scan-fr.cc/manga/'
		url_complete = url+title
		page = get_file(url_complete, title)
		manga.statut_scanfr(page)

class anime:
	def nyaa(title):
		url = 'https://nyaa.si/?f=0&c=0_0&q='
		url_complete = url+title
		#wget.download(url_complete, str(os.getcwd()+"/tmp/"+title))
		get_file(url_complete, title)
