echo off
echo ===== Estedad-V6.1 Variable font build =====
echo.
echo Generating Kashida masters:
echo ===========================
fontforge -script KashidaStyleGenerator.py Estedad Black
fontforge -script KashidaStyleGenerator.py Estedad Thin
echo Done!
echo.
echo Modifications of Kashida masters:
echo ================================================
fontforge -lang=ff -script modifications-of-Kashida-masters.pe Estedad-KThin.sfd
fontforge -lang=ff -script modifications-of-Kashida-masters.pe Estedad-KBlack.sfd
echo Done!
echo.
echo SFD to UFO Convertion:
echo ======================
fontforge -script sfd2ufo.py
echo Done!
echo.
echo writing GASP data to the generated UFOs:
echo ========================================
python save_gasp_to_ufo_files.py .\Estedad-Thin.ufo
python save_gasp_to_ufo_files.py .\Estedad-KThin.ufo
python save_gasp_to_ufo_files.py .\Estedad-Black.ufo
python save_gasp_to_ufo_files.py .\Estedad-KBlack.ufo
echo Done!
echo.
echo check_and_add_guideline_to_ufo(fontforge issue #4951):
echo ======================================================
python check_and_add_guideline_to_ufo.py .\Estedad-Thin.ufo
python check_and_add_guideline_to_ufo.py .\Estedad-KThin.ufo
python check_and_add_guideline_to_ufo.py .\Estedad-Black.ufo
python check_and_add_guideline_to_ufo.py .\Estedad-KBlack.ufo
echo Done!
echo.
echo Generating variable font:
echo =========================
fontmake -o variable -m Estedad.designspace
echo Done!
echo.
echo set fsselection bit:
echo ====================
python fsselection.py variable_ttf\Estedad-VF.ttf variable_ttf\Estedad-VF.ttf
echo Done!
echo.
echo Modify Name Records:
REM Name Records:(Args: <font-path> <string> <nameID> <platformID> <platEncID> <langID>)
echo ====================
python modify-name-records.py variable_ttf\Estedad-VF.ttf "Estedad VF" 1 3 1 0x409
python modify-name-records.py variable_ttf\Estedad-VF.ttf 6.1;amin;Estedad-VF 3 3 1 0x409
python modify-name-records.py variable_ttf\Estedad-VF.ttf "Estedad VF" 4 3 1 0x409
python modify-name-records.py variable_ttf\Estedad-VF.ttf Estedad-VF 6 3 1 0x409
echo Done!
echo.
echo add STAT table:
echo ===============
python STAT.py variable_ttf\Estedad-VF.ttf
echo Done!
echo.
echo add meta/prep/avar:
echo ===================
CMD /c ttx -m variable_ttf\Estedad-VF.ttf meta-prep-avar.ttx
python rename_move.py \meta-prep-avar.ttf \Estedad[KSHD,wght].ttf \variable_ttf
echo Done!
echo.
echo Delete Junk Files:
echo ==================
CMD /c delete_junk_files.bat
echo Done!
echo.
echo All Done!
echo.
pause