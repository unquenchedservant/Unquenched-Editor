from appdirs import *
import os, webbrowser, utilities.xml

if __name__ == "__main__":
    if sys.argv[1] == "-s":
        utilities.xml.split(sys.argv[2])
    elif sys.argv[1] == "-c":
        utilities.xml.change(sys.argv[2])
