#!/bin/zsh

cd "$(dirname "$0")"

ttx -m EstedadVF.ttf prep-gasp.ttx
python3 rename_remove.py EstedadVF.ttf prep-gasp.ttf 'Estedad[wght].ttf'

echo ""
echo "Finished. Press any key to close..."
read -n 1 -s