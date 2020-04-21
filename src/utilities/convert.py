import webbrowser, os, sys, copy, shutil
import xml.etree.ElementTree as ET
from appdirs import *

def xml_to_usfm_3(tPath, xml_path, translation, year):
    usfm_path = "{}/usfm3".format(tPath)
    if not os.path.exists(usfm_path):
        os.mkdir(usfm_path)
    ot_path = "{}/Old Testament".format(usfm_path)
    nt_path = "{}/New Testament".format(usfm_path)
    if not os.path.exists(ot_path):
        os.mkdir(ot_path)
    if not os.path.exists(nt_path):
        os.mkdir(nt_path)

    cur_path = ot_path
    x = 0

    for book in os.listdir(xml_path + "/Old Testament"):
        book_number = book.split(" ")[0][:-1]
        if len(book_number) == 1:
            book_number = "0{}".format(book_number)
        book_name = book.split(" ", 1)[1]
        if book_name == "Judges":
            book_abr = "JDG"
        elif book_name == "Song of Solomon":
            book_abr = "SNG"
        elif book_name == "Ezekiel":
            book_abr = "EZK"
        elif book_name == "Joel":
            book_abr = "JOL"
        elif book_name == "Nahum":
            book_abr = "NAM"
        else:
            book_abr = book_name.replace(" ", "")[:3]
            book_abr = book_abr.upper()
        file_name = book_number + book_abr + translation + year + ".SFM"
        file_name = file_name.upper()
        file_path = "{}/{}".format(ot_path, file_name)
        output = open(file_path, "w")
        id_line = "\\id {} {}\n".format(book_abr, file_name)
        usfm_line = "\\usfm 3.0\n"
        header_line = "\\h {}\n".format(book_name)
        output.write(id_line)
        output.write(usfm_line)
        output.write(header_line)
        tree = ET.parse(xml_path + "/Old Testament/{}/{}.xml".format(book, book_name))
        root = tree.getroot()
        ch_num = 1
        for chapter in root:
            ch_num = chapter.attrib["number"]
            output.write("\\c {}\n".format(ch_num))
            for verse in chapter:
                v_num = verse.attrib["number"]
                v_txt = verse.text
                output.write("\\v {} {}\n".format(v_num, v_txt))
        output.close()
    for book in os.listdir(xml_path + "/New Testament"):
        book_number = book.split(" ")[0][:-1]
        book_name = book.split(" ", 1)[1]
        if book_name == "Mark":
            book_abr = "MRK"
        elif book_name == "John":
            book_abr = "JHN"
        elif book_name == "Philippians":
            book_abr = "PHP"
        elif book_name == "Philemon":
            book_abr = "PHM"
        elif book_name == "James":
            book_abr = "JAS"
        elif book_name == "1 John":
            book_abr = "1JN"
        elif book_name == "2 John":
            book_abr = "2JN"
        elif book_name == "3 John":
            book_abr = "3JN"
        else:
            book_abr = book_name.replace(" ", "")[:3]
            book_abr = book_name[:3]
            book_abr = book_abr.upper()
        file_name = book_number + book_abr + translation + year + ".SFM"
        file_name = file_name.upper()
        file_path = "{}/{}".format(nt_path, file_name)
        output = open(file_path, "w")
        id_line = "\\id {} {}\n".format(book_abr, file_name)
        usfm_line = "\\usfm 3.0\n"
        header_line = "\\h {}\n".format(book_name)
        output.write(id_line)
        output.write(usfm_line)
        output.write(header_line)
        tree = ET.parse(xml_path + "/New Testament/{}/{}.xml".format(book, book_name))
        root = tree.getroot()
        ch_num = 1
        for chapter in root:
            ch_num = chapter.attrib["number"]
            output.write("\\c {}\n".format(ch_num))
            for verse in chapter:
                v_num = verse.attrib["number"]
                v_txt = verse.text
                output.write("\\v {} {}\n".format(v_num, v_txt))
        output.close()
