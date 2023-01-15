#!/usr/bin/python3
"""markdown to html"""


import sys
import os

if __name__ == "__main__":
    def errprint(*args):
        """print errors"""
        print(*args, file=sys.stderr)

    if len(sys.argv) < 3:
        errprint("Usage: ./markdown2html.py README.md README.html")
        exit(1)

    if not os.path.exists(sys.argv[1]):
        errprint("Missing {}".format(sys.argv[1]))
        exit(1)

    mdfile = open(sys.argv[1], 'r')
    htmlfile = open(sys.argv[2], 'w')
    with mdfile as md:
        with htmlfile as html:
            ulExists = False
            olExists = False
            parExists = False
            for line in mdfile:
                lenOfLine = len(line)
                heading = line.lstrip("#")
                numOfHeading = lenOfLine - len(heading)
                ulListItem = line.lstrip("-")
                ulItem = lenOfLine - len(ulListItem)
                olListItem = line.lstrip("*")
                olItem = lenOfLine - len(olListItem)

                if 1 <= numOfHeading <= 6:
                    line = "<h{}>".format(numOfHeading) + heading.strip() + "</h{}>\n".format(numOfHeading)

                if ulItem:
                    if not ulExists:
                        html.write("<ul>\n")
                        ulExists = True
                    line = "<li>" + ulListItem.strip() + "</li>\n"
                if ulExists and not ulItem:
                    html.write("</ul>\n")
                    ulExists = False

                if olItem:
                    if not olExists:
                        html.write("<ol>\n")
                        olExists = True
                    line = "<li>" + olListItem.strip() + "</li>\n"
                if olExists and not olItem:
                    html.write("</ol>\n")
                    olExists = False

                if not numOfHeading and not ulItem and not olItem:
                    if not parExists and lenOfLine > 1:
                        html.write("<p>\n")
                        parExists = True
                    elif lenOfLine > 1:
                        html.write("<br/>\n")
                    elif parExists:
                        html.write("</p>\n")
                        parExists = False

                if lenOfLine > 1:
                    html.write(line)

            if ulExists:
                html.write("</ul>\n")
            if olExists:
                html.write("</ol>\n")
            if parExists:
                html.write("</p>\n")
