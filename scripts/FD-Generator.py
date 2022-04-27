import os
import sys
import fontforge



PATH = os.path.abspath(os.getcwd()) + "\\" +sys.argv[1]

os.chdir(PATH)
for file in os.listdir():
 font = fontforge.open(file) 
 filename = os.path.splitext(file)[0]
 FNameStyle, FWeight = filename.rsplit('-',1)
 # copy Farsi digits (0 1 2 3 4 5 6 7 8 9) to Latin digits
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
 font.generate(FNameStyle + "-FD-" + FWeight + ".ttf")
