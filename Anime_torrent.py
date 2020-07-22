#!/bin/python3
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
    limite = args.limite
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
    elif limite <= 0 or limite>=50:
        print("\nInput valid limit expected.[0<P<=50]\nUse --help for more\n")
        sys.exit()
    else:
        main(title, limite)


def main(title, limite):
    try:
        from bs4 import BeautifullSoup
        import requests
    except ImportError as error:
        print(error)
        print('Please install it with $pip install')


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="A simple torrent search tool.")
	parser.add_argument("title", help="Enter search string", nargs="?", default=None)
	parser.add_argument("-l", "--limite", type=int, help="Number of pages to fetch results from (1 page = 30 results).\n [default: 1]", default=1, dest="limite")
	parser.add_argument("-c", "--clear", action="store_true", default=False, help="Clear all torrent description HTML files and exit.")
	args = parser.parse_args()
	init(args)
