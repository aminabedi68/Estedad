import sys
import fontforge

font = fontforge.open(sys.argv[1])
for glyph in font.glyphs() :
 if glyph.color == 0x00ffff :
  font.selection.select(("more",None),glyph)
font.activeLayer = 0
font.round()
font.save()