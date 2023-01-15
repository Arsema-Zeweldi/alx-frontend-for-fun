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
