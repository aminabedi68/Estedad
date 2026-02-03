#!/bin/zsh

cd "$(dirname "$0")"
python3 supportedCharset.py 'Estedad[wght].ttf'

echo ""
echo "Finished. Press any key to close..."
read -n 1 -s