from fuzzywuzzy import fuzz
from fuzzywuzzy import process


books = ["GENESIS", "EXODUS", "LEVITICUS",
         "NUMBERS", "DEUTERONOMY", "JOSHUA",
         "JUDGES", "RUTH", "1 SAMUEL", "2 SAMUEL",
         "1 KINGS", "2 KINGS", "1 CHRONICLES", "2 CHRONICLES",
         "EZRA", "NEHEMIAH", "ESTHER", "JOB", "PSALM", "PROVERBS",
         "ECCLESIASTES", "SONG OF SOLOMON", "ISAIAH", "JEREMIAH",
         "LAMENTATIONS", "EZEKIEL", "DANIEL", "HOSEA", "JOEL", "AMOS",
         "OBADIAH", "JONAH", "MICAH", "NAHUM", "HABAKKUK", "ZEPHANIAH",
         "HAGGAI", "ZECHARIAH", "MALACHI", "MATTHEW", "MARK", "LUKE", "JOHN",
         "ACTS", "ROMANS", "1 CORINTHIANS", "2 CORINTHIANS", "GALATIANS",
         "EPHESIANS", "PHILIPPIANS", "COLOSSIANS", "1 THESSALONIANS", "2 THESSALONIANS",
         "1 TIMOTHY", "2 TIMOTHY", "TITUS", "PHILEMON", "HEBREWS", "JAMES", "1 PETER",
         "2 PETER", "1 JOHN", "2 JOHN", "3 JOHN", "JUDE", "REVELATION"]
def get_abbreviations(full):
    full = full.upper()
    best_guess = ""
    for i in range(len(books)):
        best_guess = compare(best_guess, books[i], full)
    return best_guess

def compare(str1, str2, full):
    check1 = check_ratio(str1, full)
    check2 = check_ratio(str2, full)
    if check1 > check2:
        return str1
    else:
        return str2
def check_ratio(orig, checking):
    return fuzz.partial_ratio(orig, checking)
