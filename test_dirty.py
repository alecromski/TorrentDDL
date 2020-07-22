def main():
    from tabulate import tabulate
    header = ["Select", "Name", "Description"]
    select_source = [["1", "Nyaa torrent", "Anime torrent tracker"], ["2", "TorrentZ²", "torrentz² search engine"]]
    print(tabulate(select_source, header, tablefmt="fancy_grid"))
    select = input()
    if select == None:
        main()
    elif select == '1':
        Downloadfile(title)
    elif select == '2':
        Downloadfile(title)
    else:
        print("Know what you want befor you nerd")
        sys.exit()
main()
