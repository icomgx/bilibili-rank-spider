# coding: utf-8

from sys import argv

argc = len(argv)


def help():
    print("""Usage: 
    {0} webui\t- startup a WebUI.""".format(argv[0]))


if argc == 1:
    help()
elif argv[1] == "webui":
    import webui
    webui.main()
else:
    help()