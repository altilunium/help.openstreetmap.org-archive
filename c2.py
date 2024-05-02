import os
import json
import sys
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

with open('output2.json') as f:
    data = json.load(f)

cwd = os.getcwd()
qa = set()
for item in data:
    print(item)
    aa = cwd +"\\"+ str(item) + "\\index.html" 
    print(aa)
    with open(aa, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        e = soup.find(id="CALeft")
        #e.insert(0,"<center><a href='../'><img id='ll' src='https://help.openstreetmap.org/upfiles/osm_help_logo_6.png'></a></center>")

        soup2 = BeautifulSoup("<center></center>",'html.parser')
        original_tag = soup2.center
        new_tag = soup2.new_tag("a", href="../")
        original_tag.append(new_tag)
        new_tag2 = soup2.new_tag("img", id="ll", src="https://help.openstreetmap.org/upfiles/osm_help_logo_6.png")
        new_tag.append(new_tag2)
        e.insert(0,original_tag)


        #print(soup)
      
        with open(aa, 'w', encoding='utf-8') as z:
            z.write(str(soup))
        



for dirpath, dirnames, filenames in os.walk(cwd):
    print(dirpath)
    break