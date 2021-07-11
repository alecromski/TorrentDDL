#!/usr/bin/python3
try:
	import requests, os, sys, argparse
	from os import listdir
	from media import anime
	from media import manga    
except ImportError as e:
	print(e)
	print("Please install it with pip3 install")
	sys.exit()

def switch(name, char):
	var_mod = []
	for i in range(0,len(name)):
		if name[i]== " ":
			var_mod.append(char)
		else:
			var_mod.append(name[i])
	final_var = "".join(var_mod)
	return(final_var)

def title(name, site):
	if site == "nyaa.si":
		name = switch(name, "+")
	elif site == "scan-fr":
		name = switch(name, "-")
	return name

def manga_anime():
	print("\n1) anime from site\n2) manga from site\n")
	result = input('choose your media:')
	return result

def init(args):
	if args.clear:
		temp_dir = os.getcwd()+'/tmp'
		temp_files = os.listdir(temp_dir) 
		if not temp_files:
			print("\nNothing to remove")
		else:
			count = 0
			for i in temp_files:
				os.remove(os.path.join(temp_dir, i))
				count = count+1
			print("Removed %d file(s)." % count)
	if args.title == None:
		print("\nInput string expected.\nUse --help for more\n")
		sys.exit()
	else:
		media = manga_anime()
		if media == "1":
			title_full = title(args.title, "nyaa.si")
			anime.nyaa(title_full)
		elif media == "2":
			title_full = title(args.title, "scan-fr")
			manga.scanfr(title_full)
		else:
			print("Select properly with the index")
			
		print(title_full)


parser = argparse.ArgumentParser(description="A simple torrent search tool.")
parser.add_argument("title", help="Enter search string", nargs="?", default=None)
parser.add_argument("-c", "--clear", help="Clear all torrent description HTML files and exit.", required=False)
args = parser.parse_args()
init(args)