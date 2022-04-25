import os, sys
from os import path
import shutil

cwd = os.getcwd()

old_name = sys.argv[1]
new_name = sys.argv[2]
folder_name = sys.argv[3]

old_namepath = str(cwd + old_name)
new_namepath = str(cwd + new_name)
filepath = str(cwd) + str(folder_name) + new_name

# Removing old file
files_to_remove = [new_name]
for Dfile in files_to_remove:
 try:
  os.remove(cwd + Dfile)
 except WindowsError:
  pass

# Renaming new file
os.rename(old_namepath,new_namepath)

# Moving new file
shutil.move(new_namepath, filepath)

