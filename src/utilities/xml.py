import webbrowser, os, sys, copy, shutil
import xml.etree.ElementTree as ET
from appdirs import *

appname = "unquenched-editor"
appauthor = "Unquenched Servant"
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
        tree = ET.parse(file_path)
        bible = tree.getroot()
        abbvr = input("Please enter translation abbreviation: ")
        root_path = "{}/{}".format(user_data_dir(appname, appauthor), abbvr)
        if not os.path.exists(root_path):
            os.makedirs(root_path)
        tYear = input("Please enter year of version: ")
        version_path = "{}/{}".format(root_path, tYear)
        if not os.path.exists(version_path):
            os.mkdir(version_path)
        xml_path = "{}/{}".format(version_path, "xml")
        if not os.path.exists(xml_path):
            os.mkdir(xml_path)
        if not os.path.exists("{}/Old Testament".format(xml_path)):
            os.mkdir("{}/Old Testament".format(xml_path))
        if not os.path.exists("{}/New Testament".format(xml_path)):
            os.mkdir("{}/New Testament".format(xml_path))

        x = 1 #for starting folder names
        is_OT = True



        if not bible.tag == "bible":
            change(file_path)

        testament_path = "{}/Old Testament".format(xml_path)
        for book in bible:
            if not book.tag == "book":
                change(file_path)
            title = book.attrib["title"]
            if title == "Matthew":
                is_OT = False
                x = 41
                testament_path = "{}/New Testament".format(xml_path)
            book_path = "{}/{}. {}".format(testament_path, x, title)
            if not os.path.exists(book_path):
                os.mkdir("{}".format(book_path))


            book_data = ET.tostring(book).decode('utf-8')
            book_file = open("{}/{}.xml".format(book_path, title), "w")
            book_file.write(book_data)
            book_file.close()
            x += 1
            for chapter in book:
                if not chapter.tag == "chapter":
                    change(file_path)
                ch_number = chapter.attrib["number"]
                write_path = "{}/{} {}.xml".format(book_path, title, ch_number)
                chapter_data = ET.tostring(chapter).decode('utf-8')
                chapter_file = open(write_path, "w")
                chapter_file.write(chapter_data)
                chapter_file.close()
        shutil.copyfile(file_path, "{}/full.xml".format(version_path))

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
