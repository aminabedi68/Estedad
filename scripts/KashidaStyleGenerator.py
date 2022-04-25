import os
import sys
import fontforge

FontName = str(sys.argv[1])
FontStyle = str(sys.argv[2])
NewFontStyle = "K" + FontStyle

font = fontforge.open(FontName + "-" + FontStyle + ".sfd")
font.fontname = FontName + "-" + NewFontStyle
font.familyname = FontName + " " + FontStyle
font.fullname = FontName + " " + FontStyle
for glyph in font.glyphs() :
 if glyph.color == 0x00ffff : #select all glyphs with cyan color
  glyph.setLayer(glyph.layers['Back'], 'Fore')
  GLSB = glyph.right_side_bearing
  GLSB = int(GLSB)
  GLSB += 2048
  glyph.right_side_bearing = GLSB
font.appendSFNTName('English (US)' , 'Preferred Styles' , NewFontStyle)
font.save(FontName + "-" + NewFontStyle + ".sfd")