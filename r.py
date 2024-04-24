import json
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

with open('qnadump_88268.json') as f:
    data = json.load(f)

for i in data:
    nya = '<meta charset="UTF-8"><link rel="stylesheet" type="text/css" href="../style.css">' + i['text']
    os.makedirs(str(i['id']), exist_ok=True)
    file_path = os.path.join(str(i['id']), 'index.html')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(nya)
