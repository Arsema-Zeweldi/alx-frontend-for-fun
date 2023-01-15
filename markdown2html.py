#!/usr/bin/python3
"""markdown to html"""


import sys
import os
import markdown
from mdutils.mdutils import MdUtils
from mdutils import Html


def errprint(*args):
    print(*args, file=sys.stderr)


if len(sys.argv) < 3:
    errprint("Usage: ./markdown2html.py README.md README.html")
    raise SystemExit(1)
else:
    path = "./"
    if os.path.exists(sys.argv[1]):
        markdown.markdownFromFile(input=sys.argv[1], output=sys.argv[2])
    else:
        errprint("Missing ", sys.argv[1])
        raise SystemExit(1)
