import os
from os import path
import fontforge
import shutil

glyphs_to_unlink = ["exclamdown","hookabovecomb","questiondown","uni018E","uni01DD","uni0245","uni0250","uni029E","uniE01C","uniE0A1","uni0657","uni065E","uniE01E","uniE01F","Ohungarumlaut","uni0200","Arabic_Double_Dot_H","Arabic_Double_Dot_V","Arabic_Triple_Dot_Up","Arabic_Triple_Dot_Down","Arabic_Triple_Dot_H","Arabic_Quadruple_Dot","uni0652","j","Oslash","oslash","uni030F","hungarumlaut"]

for file in os.listdir():
 if file.endswith(".sfd"):
  font = fontforge.open(file)
  for glyph in font.glyphs():
   if glyph.glyphname in glyphs_to_unlink:
    font.selection.select(glyph.glyphname)
    glyph.unlinkRef()
    glyph.round()
  font.generate(os.path.splitext(file)[0]+".ttf")

if not path.exists(os.getcwd() + "\master_ttf"):
 os.mkdir(os.getcwd() + "\master_ttf")

sourcepath = os.getcwd()
sourcefiles = os.listdir(sourcepath)
destinationpath = os.getcwd() + "\master_ttf"
for file in sourcefiles:
 if file.endswith('.ttf'):
  shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))