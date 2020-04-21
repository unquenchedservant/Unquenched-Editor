import webbrowser, os, sys
import xml.etree.ElementTree as ET


def split(file_path):
    if check_file(file_path):
        pass

def check_file(file_path):
    if not os.path.exists(file_path):
        print("ERROR: File not found")
        sys.exit()
    if not file_path.endswith(".xml"):
        print("ERROR: File is not an xml file")
        sys.exit()
    if os.path.isdir(file_path):
        print("ERROR: Path is a directory")
        sys.exit()
    return True
