import os
import sys
import fontforge



PATH = os.path.abspath(os.getcwd()) + "\\" +sys.argv[1]

os.chdir(PATH)
for file in os.listdir():
 font = fontforge.open(file) 
 filename = os.path.splitext(file)[0]
 FNameStyle, FWeight = filename.rsplit('-',1)
 mapDigits = {
     "uni06F0": "zero",
     "uni0661": "one",
     "uni0662": "two",
     "uni0663": "three",
     "uni06F4": "four",
     "uni06F5": "five",
     "uni06F6": "six",
     "uni0667": "seven",
     "uni0668": "eight",
     "uni0669": "nine",
 }
 for index in mapDigits:
     font.selection.select(index)
     font.copyReference()
     font.selection.select(mapDigits[index])
     font.paste()
 font.selection.none()
 font.fontname = FNameStyle + "-FD-" + FWeight
 font.familyname = FNameStyle + "-FD " + FWeight
 font.fullname = FNameStyle + "-FD " + FWeight
 PreferredFamily = FNameStyle + "-FD "
 PreferredStyles = FNameStyle + "-FD-" + FWeight
 font.appendSFNTName('English (US)' , 'Preferred Family' , PreferredFamily)
 font.appendSFNTName('English (US)' , 'Preferred Styles' , PreferredStyles)
 # font.removeLookup("'ss07' Style Set 7 lookup 24")
 # font.removeLookup("'ss08' Style Set 8 lookup 25")
 # font.removeLookup("'ss09' Style Set 9 lookup 26")
 # font.removeLookup("'ss10' Style Set 10 lookup 27")
 # font.removeLookup("'ss11' Style Set 11 lookup 28")
 font.generate(FNameStyle + "-FD-" + FWeight + ".ttf")