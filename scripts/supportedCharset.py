import os
import sys
from fontTools.ttLib import TTFont

font_path = os.path.abspath(os.getcwd()) + "\\" +sys.argv[1]
f = TTFont(font_path)
cmap = f.getBestCmap()
for char in sorted(cmap):
    print(chr(char), end =" ")