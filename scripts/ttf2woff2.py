import os
import sys
from os import path
from fontTools.ttLib import TTFont
import shutil

ttf_path = os.path.abspath(os.getcwd()) + "\\" +sys.argv[1]
os.chdir(ttf_path)

for file in os.listdir(): 
 if file.endswith(".ttf"):
  f = TTFont(file)
  f.flavor='woff2'
  f.save(os.path.splitext(file)[0]+".woff2")

if not path.exists("woff2"):
 os.mkdir("woff2")
sourcefiles = os.listdir(ttf_path)
destenation_path = ttf_path + "\woff2"
for file in sourcefiles:
    if file.endswith('.woff2'):
        shutil.move(os.path.join(ttf_path,file), os.path.join(destenation_path,file))