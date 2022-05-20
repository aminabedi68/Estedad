echo off
CMD /c build_variable_font.bat
CMD /c build_instances.bat
CMD /c FD-Generator.bat
CMD /c ttf2woff2.bat
pause
