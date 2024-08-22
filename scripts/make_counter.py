#This code scrapes the exoplanet archive for the number of
#exoplanets


import pandas as pd
import numpy as np
import os, sys
import urllib.request
from datetime import date
import requests
from bs4 import BeautifulSoup

def lines_that_contain(string, fp):
    return [line for line in fp if string in line]

url = "https://exoplanetarchive.ipac.caltech.edu/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
job_date= soup.find_all("div", class_="date")
job_stat = soup.find_all("div", class_="stat")

dates = [job_date[0].text.strip(),job_date[1].text.strip(),job_date[2].text.strip()]
stat = [job_stat[0].text.strip(),job_stat[1].text.strip(),job_stat[2].text.strip()]

#Convert str into int
conf_planets = int(stat[0].replace(',', ''))

#Get the current date 
current_date = date.today()
start_date = date(2018,7,25)
delta_date = current_date - start_date


#Get the number of publications


pub_file = "./tpub.db"
if os.path.exists(pub_file):
    os.remove(pub_file)
#Get the tpub file
urllib.request.urlretrieve("https://github.com/tessgi/tpub/raw/master/data/tpub.db", filename=tpub_path)
query = sqlite3.connect(pub_file).execute("SELECT * FROM pubs")
cols = [column[0] for column in query.description]
results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
results = results[results["mission"] == "tess"].reset_index(drop=True)
pub_stat = len(results)

#Now need to create the file
#opens the template
template_file = "planet_counter.html"
file_out = "../themes/pelican-bootstrap3-tess/templates/includes/planet_counter.html"

with open(template_file, 'r') as file:
    filedata = file.read()

#replace the target string
filedata = filedata.replace("data-target=446", "data-target="+str(conf_planets))
filedata = filedata.replace("data-target=2227", "data-target="+str(delta_date.days))
filedata = filedata.replace("data-target=2106", "data-target="+str(pub_stat))

if os.path.exists(file_out):
    os.remove(file_out)

# Write the file out again
with open(file_out, 'w') as file:
  file.write(filedata)
