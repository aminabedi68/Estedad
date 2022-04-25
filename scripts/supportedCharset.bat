@echo off
fontforge -lang=ff -script generate.pe Estedad-Black.sfd Estedad-Black.ttf
python supportedCharset.py Estedad-Black.ttf
CMD /c delete_junk_files.bat
pause