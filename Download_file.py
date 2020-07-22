#!/usr/bin/python3
try:
    import wget, os
    from os import listdir
except ImportError as e:
    print(e)
    print("Please install it with $pip3 install")
    sys.exit()

def nyaa(title):
    url = 'https://nyaa.si/?f=0&c=0_0&q='
    url_complete = url+title
    home = os.path.expanduser("~")
    temp_dir = home+"/GIT/Torse/tmp"
    temp_name = temp_dir+"/nyaa_"+title+".html"
    wget.download(url_complete, str(temp_name))

def torrentsquare(title):
    url = 'https://torrentz2.is/search?f='
    url_complete = url+title
    home = os.path.expanduser("~")
    temp_dir = home+"/GIT/Torse/tmp"
    temp_name = temp_dir+"/torrentsquare_"+title+".html"
    wget.download(url_complete, str(temp_name))
