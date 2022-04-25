import os
import sys
import linecache
 
PATH = sys.argv[1]
os.chdir(PATH)

with open('fontinfo.plist') as f:
    if '<key>guidelines</key>' in f.read():
     sys.exit()
    else:
     file_read = open('fontinfo.plist', "r")
     num_lines = sum(1 for line in open('fontinfo.plist'))
     BreakLine = num_lines - 2
     # guidelines key:
     section_2 = "    <key>guidelines</key>\n"
     # Before:
     section_1 = ""
     l = 0
     while l < BreakLine:
      section_1 = section_1 + linecache.getline('fontinfo.plist', l)
      l += 1
     # after:
     section_3 = ""
     l = BreakLine
     while True:
      section_3 = section_3 + linecache.getline('fontinfo.plist', l)
      l += 1
      if (linecache.getline('fontinfo.plist', l) == ""):
       break
     # new fontinfo:
     data = section_1 + section_2 + section_3
     fontinfo = open("fontinfo.plist" , "w")
     fontinfo.write(data)
     fontinfo.close()