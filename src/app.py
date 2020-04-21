from appdirs import *
import os, webbrowser, utilities.xml, utilities.convert, sys
appname = "unquenched-editor"
appauthor = "Unquenched Servant"
if __name__ == "__main__":
    if sys.argv[1] == "-t":
        if sys.argv[2] == "xml":
            if sys.argv[3] == "-s":
                utilities.xml.split(sys.argv[4])
            elif sys.argv[3] == "-f":
                utilities.xml.change(sys.argv[4])
            elif sys.argv[3] == "-c":
                if len(sys.argv) > 4:
                    translation = sys.argv[4]
                else:
                    print("Please include the translation abbreviation")
                    sys.exit()
                if len(sys.argv) > 5:
                    year = sys.argv[5]
                else:
                    print("Please include the translation year")
                    sys.exit()
                if not os.path.exists("{}/{}".format(user_data_dir(appname, appauthor), translation)):
                    print("Translation does not exist")
                    sys.exit()
                tPath = "{}/{}/{}".format(user_data_dir(appname, appauthor), translation, year)
                if not os.path.exists("{}".format(tPath)):
                    print("Invalid year")
                    sys.exit()
                final_path = "{}/xml".format(tPath)
                if not os.path.exists("{}".format(final_path)):
                    print("No XML path exists for this translation and year")
                    sys.exit()
                utilities.convert.xml_to_usfm_3(tPath, final_path, translation, year)
    else:
        print("Please use -t for specifying the type")
