import os
import fontforge

for file in os.listdir(): 
 if file.endswith(".sfd"):
  font = fontforge.open(file)
  for glyph in font.glyphs():
   font.selection.select(("more",None),glyph)
  font.round()
  font.save()