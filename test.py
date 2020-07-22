#!/usr/bin/python3
import argparse, os, sys
from os import listdir

def space(variable):
    var_mod = []
    for i in range(0,len(variable)):
        if variable[i]== " ":
            var_mod.append("+")
        else:
            var_mod.append(variable[i])
    final_var = "".join(var_mod)
    return(final_var)

def init(args):
    title = args.title
    title = space(title)
    if args.clear:
        home = os.path.expanduser("~")
        temp_dir = home+"/GIT/Torse/tmp"
        temp_files = os.listdir(temp_dir) 
        if not temp_files:
            print("\nNothing to remove\n")
        else:
            count = 0
            for i in temp_files:
                os.remove(os.path.join(temp_dir, i))
                count = count+1
            print("\nRemoved %d file(s)." % count)
    if title == None:
        print("\nInput string expected.\nUse --help for more\n")
        sys.exit()
    else:
        select_source(title)


def select_source(title):
    from tabulate import tabulate
    import Download_file
    header = ["Select", "Name", "Description"]
    select_source = [["1", "Nyaa torrent", "Anime torrent tracker"], ["2", "TorrentZ²", "torrentz² search engine"]]
    print(tabulate(select_source, header, tablefmt="fancy_grid"))
    select = input()
    if select == None:
        select_source()
    elif select == '1':
        Download_file.nyaa(title)
    elif select == '2':
        Download_file.torrentsquare(title)
    else:
        print("Know what you want befor you nerd")
        sys.exit()


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="A simple torrent search tool.")
	parser.add_argument("title", help="Enter search string", nargs="?", default=None)
	parser.add_argument("-c", "--clear", action="store_true", default=False, help="Clear all torrent description HTML files and exit.")
	args = parser.parse_args()
	init(args)
