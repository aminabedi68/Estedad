import os
import os.path
import shutil

path = os.getcwd()
dirs_to_remove = ["\Estedad-Black.ufo","\Estedad-Bold.ufo","\Estedad-KBlack.ufo","\Estedad-KBold.ufo","\Estedad-KThin.ufo","\Estedad-Thin.ufo","\instance_ufo","\master_ttf"]

for Ddir in dirs_to_remove:
 try:
  shutil.rmtree(path + Ddir)
 except WindowsError:
  pass

files_to_remove = ["\Estedad-KBlack.sfd","\Estedad-KBold.sfd","\Estedad-KThin.sfd","\Estedad-Black.ttf","\variable_ttf\Estedad-VF.ttf"]

for Dfile in files_to_remove:
 try:
  os.remove(path + Dfile)
 except WindowsError:
  pass

path = path + "\\variable_ttf"
files_to_remove = ["\Estedad-VF.ttf"]

for Dfile in files_to_remove:
 try:
  os.remove(path + Dfile)
 except WindowsError:
  pass