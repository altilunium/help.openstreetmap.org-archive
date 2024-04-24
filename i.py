import os
import requests
from bs4 import BeautifulSoup
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')


# Set the current working directory
cwd = os.getcwd()

pts = 0

db = dict()

# Loop through all subdirectories in the current directory
for dirpath, dirnames, filenames in os.walk(cwd):
    # Check if the subdirectory contains an index.html file
    if 'index.html' in filenames:
        # Open the index.html file and parse it with BeautifulSoup
        with open(os.path.join(dirpath, 'index.html'), 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        # Process the DOM of the index.html file
        # For example, you can print the title of the page
        try:
            search_results = soup.find('div', class_='headNormal')
            a_tag = search_results.find('a')
            text = a_tag.text
            search_results = soup.find('div', class_='post-score')
            score = search_results.text.strip()
            print(os.path.basename(dirpath),text,score)
            db[os.path.basename(dirpath)] = dict()
            db[os.path.basename(dirpath)]["title"] = text
            db[os.path.basename(dirpath)]["score"] = score

        except Exception as e:
            pass

        pts = pts + 1
        print(pts)
        


with open('output.json', 'w') as f:
    json.dump(db, f)