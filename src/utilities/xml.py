import webbrowser, os, sys
import xml.etree.ElementTree as ET

def change(file_path):
    if check_file(file_path):
        #open xml for checking
        webbrowser.open(file_path)
        #enter the current tags for comparison
        book_tag = input("Enter Book Tag: ")
        chapter_tag = input("Enter Chapter Tag: ")
        verse_tag = input("Enter Verse Tag: ")
        number_attr = input("Enter Number Attr: ")

        tree = ET.parse(file_path)

        if not tree.getroot().tag == "bible":
            tree.getroot().tag = "bible"
        if not book_tag == "book":
            for elem in tree.findall(book_tag):
                elem.tag = "book"
        if not chapter_tag == "chaptr":
            for elem in tree.findall("book/{}".format(chapter_tag)):
                elem.tag = "chapter"
                if not number_attr == "number":
                    num = elem.attrib[number_attr]
                    elem.attrib.pop(number_attr, None)
                    elem.set("number", "{}".format(num))
        if not verse_tag == "vere":
            for elem in tree.findall("book/chapter/{}".format(verse_tag)):
                elem.tag = "verse"
                if not number_attr == "number":
                    num = elem.attrib[number_attr]
                    elem.attrib.pop(number_attr, None)
                    elem.set("number", "{}".format(num))
        tree.write(file_path)

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
