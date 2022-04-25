import os, sys
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._n_a_m_e import NameRecord

fontPath = sys.argv[1]
font = TTFont(fontPath)
# setName(text, int(name_id), int(platform_id), int(plat_enc_id), int(lang_id, 16))
font['name'].setName(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6], 16))
font.save(fontPath)