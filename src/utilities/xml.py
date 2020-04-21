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
        title_attr   = input("Enter the Book Title Attribute: ")

        tree = ET.parse(file_path)

        if not tree.getroot().tag == "bible":
            tree.getroot().tag = "bible"
        tree = changer(tree, book_tag, book_tag, "book", title_attr, "title")
        tree = changer(tree, "book/{}".format(chapter_tag), chapter_tag, "chapter", number_attr, "number")
        tree = changer(tree, "book/chapter/{}".format(verse_tag), verse_tag, "verse", number_attr, "number")
        tree.write(file_path)

def changer(tree, xpath, search_tag, wanted, attr, wanted_attr):
    if not search_tag == wanted:
        for elem in tree.findall(xpath):
            elem.tag = wanted
            if not attr == wanted_attr:
                temp = elem.attrib[attr]
                elem.attrib.pop(attr, None)
                elem.set("{}".format(wanted_attr), "{}".format(temp))
    return tree

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
