import os
import fontforge

os.chdir(".\instance_ttf")
for file in os.listdir(): 
	if file.endswith(".ttf"):
		font = fontforge.open(file)
		for glyph in font.glyphs():
		 glyph.round()
		font.generate(os.path.splitext(file)[0]+".ttf")
