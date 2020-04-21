from appdirs import *
import os, webbrowser, utilities.xml
appname = "unquenched-editor"
appauthor = "Unquenched Servant"
if __name__ == "__main__":
    if sys.argv[1] == "-s":
        utilities.xml.split(sys.argv[2])
    elif sys.argv[1] == "-c":
        utilities.xml.change(sys.argv[2])
    elif sys.argv[1] == "-p":
        print(user_data_dir(appname, appauthor))
