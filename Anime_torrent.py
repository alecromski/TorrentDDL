import os
import sys
import argparse

def start(args):
    title = args.title
    title = print(string.replace(" ", ""))  
    limite = args.limite
    if args.clear:
        home = os.path('~')
        temp_dir = home+"/.local/bin/torse/temp/"
        temp_files = os.listdir(temp_dir)
    if not temp_files:
        print("\nNothing to remove\n")
    else:
        for i in temp_files:
            os.remove(os.path.join(temp_dir, i))
            count = count+1
            print("\nRemoved %d file(s)." %count)
    if title == None:
        print("\nInput string expected.\nUse --help for more\n")
        sys.exit()
    elif limite <= 0 or limit>=50:
        print("\nInput valid limit expected.[0<P<=50]\nUse --help for more\n")
        sys.exit()
    else:
        main(title, limite)

def main(title, limite):
    try:
        import request
        from bs4 import BeautifullSoup
        from tabulate import tabulate
        from termcolor import colored
        url = 'https://nyaa.si/?f=0&c=0_0&q=+title'
    except ImportError as error:
        print(error)
        print("Please install and retry.\n")
        sys.exit()

    