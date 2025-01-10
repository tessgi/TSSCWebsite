#!/usr/bin/env python3
from glob import glob
import os
import numpy as np
import pandas as pd
import re
from tqdm import tqdm

#PROPOSALS_URL = "https://heasarc.gsfc.nasa.gov/docs/tess/proposals/"
# TARGETS_URL = "https://heasarc.gsfc.nasa.gov/docs/tess/targets"

PROPOSALS_URL = "https://heasarc.gsfc.nasa.gov/docs/tess/data/approved-programs/"
TARGETS_URL = "https://heasarc.gsfc.nasa.gov/docs/tess/data/target_lists"

approved_programs = pd.read_csv('content/data/approved-programs/approved_program_list.csv').values
fnames = np.sort(glob("content/data/approved-programs/cycle*/*.txt"))

attrs = ['Title', 'PI', 'Type', 'Summary']
htmlstrs = []
for fname in tqdm(fnames):
    txt = open(fname).read()
    data = {attr:re.search(rf'{attr}:\s*(.*?)\n', txt).group(1).strip() for attr in attrs}
    data['PI'], data['Institute'] = data['PI'].split(' - ')
    data['Proposal ID'] = fname.split('/')[-1][:-4]
    if data['Type'] == 'N/A':
        data['Type'] = 'Small'
    data['Type'] = data['Type'].capitalize()
    cycle = fname.split('/')[-2][5:]
    data['Cycle'] = f"Cycle {cycle}"
    #if data['Proposal ID'] in approved_programs:
    if data['Proposal ID'] in approved_programs:
        selected = 'True'
    else:
        selected = 'False'
    htmlstrs.append(f"""
    <tr>
        <th scope="row">{data['Proposal ID']}</th>
        <td>{data['PI']}</td>
        <td>
            <div class="accordion accordion-flush" id="accordion{data['Proposal ID']}">
                <div class="accordion-item">
                    <h2 class="accordion-header" id="flush-heading{data['Proposal ID']}">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                        data-bs-target="#flush-collapse{data['Proposal ID']}" aria-expanded="false" aria-controls="flush-collapse{data['Proposal ID']}">
                        {data['Title']}
                    </button>
                    </h2>
                    <div id="flush-collapse{data['Proposal ID']}" class="accordion-collapse collapse" aria-labelledby="flush-heading{data['Proposal ID']}"
                    data-bs-parent="#accordion{data['Proposal ID']}">
                    <div class="accordion-body">
                    <a href="{PROPOSALS_URL}{fname.split('/')[-2]}/{data['Proposal ID']}.txt"target="_blank">{data['Proposal ID']} Targets </a>
                    <br></br>
                    {data['Summary']}
                    <br></br>
                    </div>
                    </div>
                </div>
            </div>
        </td>
        <td>{data['Cycle']}</td>
        <td>{data['Type']}</td>
        <td>{selected}</td>
    </tr>
    """)

rows = '\n'.join(htmlstrs)

htmlstr = f"""<table data-toggle="table" data-pagination="true" data-search="true" id="searchabletable" class="table table-bordered">
    <caption>Table of the Approved TESS Programs</caption>
    <thead class="thead-dark">
        <tr>
            <th data-sortable="true" data-field="id" scope="col">Proposal ID</th>
            <th data-field="pi" scope="col">PI </th>
            <th data-field="title" scope="col">Title</th>
            <th data-sortable="true" data-field="cycle" scope="col">Cycle</th>
            <th data-sortable="true" data-field="type" scope="col">Type</th>
            <th data-sortable="true" data-field="selected" scope="col">Selected</th>
        </tr>
    </thead>
    <tbody>
    {rows}
    </tbody>
    </thead>
</table>"""

with open("htmlcontent/tables/approved-programs.table.html", "w") as file:
    file.write(htmlstr)
