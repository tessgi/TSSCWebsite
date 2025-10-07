import re
from datetime import date, datetime
import pandas as pd
import glob

# This file is to be used for a cronjob to update time-dependent components of the website. 
SCIENCE_DAYS = (date.today() - date.fromisoformat('2018-07-18')).days


# Current sector for where is tess button
sec_dates = pd.read_csv('/Users/rhounsel/Desktop/TESS/TSSCWebsite/content/data/TESS_orbit_times.csv') #https://tess.mit.edu/observations/
for index, row in sec_dates.iterrows():
    if ((datetime.today() < datetime.strptime(row['End of Orbit'], "%Y-%m-%d %H:%M:%S")) & (datetime.today() >= datetime.strptime(row['Start of Orbit'], "%Y-%m-%d %H:%M:%S"))):
        CURRENT_SECTOR = row['Sector']


# Replace the "where is TESS" button pointer and the "Days of Science" count
# Because of the pagination, there are multiple index files that need to update
index_files = glob.glob("/Users/rhounsel/Desktop/TESS/TSSCWebsite/output/index*.html")
for f in index_files:
    with open(f,'r') as currentfile:
        data = currentfile.readlines()
        
    pattern1 = r"sector.*_summary\.html"
    pattern2 = r"Days of Science"
    for i, line in enumerate(data):
        if re.search(pattern1, line):
            data[i] = f'                <a href="sector{CURRENT_SECTOR}_summary.html">\n'
        if re.search(pattern2, line):
            data[i+4] = f'            <div class="col-sm-2 counter" data-target="{SCIENCE_DAYS}">0</div>\n'

    with open(f, 'w', encoding='utf-8') as file:
        file.writelines(data)



