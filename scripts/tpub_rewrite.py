import pandas as pd
import numpy as np
import os, sys


dir = 'content/pages/tpub/'

def file_change(filename_list_in,
                chec_words_list,
                rep_words_list,
                filename_list_out):

    for a in range(len(filename_list_in)):

        fin = open(str(dir)+str(filename_list_in[a]), 'r')
        fout = open(str(dir)+str(filename_list_out[a]), 'w')

        for line in fin:
            for check, rep in zip(chec_words_list[a], rep_words_list[a]):
                line = line.replace(check, rep)
            fout.write(line)
        fin.close()
        fout.close()

        os.remove(str(dir)+str(filename_list_in[a]))
        os.rename(str(dir)+str(filename_list_out[a]),str(dir)+str(filename_list_in[a]))

    return


cw1 = ["Save_as: publications.html","[TOC]","## Publication database","![Publication rate by year](images/tpub/tpub-publication-rate.png)","![Publications by subject](images/tpub/tpub-piechart.png)"]
rp1 = ["template: slide\nSave_as: publications.html","", "<h2>Publication database</h2>","![Publication rate by year](images/statistics/publications_barchart.png)","![Publications by subject](images/statistics/publications_piechart.png)"]

cw2 = ["Save_as: tpub-astrophysics-by-month.html","[TOC]"]
rp2 = ["template: slide\nSave_as: tpub-astrophysics-by-month.html",""]

cw3 = ["Save_as: tpub-astrophysics.html","[TOC]"]
rp3 = ["template: slide\nSave_as: tpub-astrophysics.html",""]

cw4 = ["Save_as: tpub-by-month.html","[TOC]"]
rp4 = ["template: slide\nSave_as: tpub-by-month.html",""]

cw5 = ["Save_as: tpub-exoplanets-by-month.html","[TOC]"]
rp5 = ["template: slide\nSave_as: tpub-exoplanets-by-month.html",""]

cw6 = ["Save_as: tpub-exoplanets.html","[TOC]"]
rp6 = ["template: slide\nSave_as: tpub-exoplanets.html",""]

cw7 = ["Save_as: tpub.html","[TOC]"]
rp7 = ["template: slide\nSave_as: tpub.html",""]

check_list=[cw1,cw2,cw3,cw4,cw5,cw6,cw7]
rep_list=[rp1,rp2,rp3,rp4,rp5,rp6,rp7]


filename_list_in = ['publications.md',
                    'tpub-astrophysics-by-month.md',
                    'tpub-astrophysics.md',
                    'tpub-by-month.md',
                    'tpub-exoplanets-by-month.md',
                    'tpub-exoplanets.md',
                    'tpub.md']
                    
filename_list_out = ['publications2.md',
                     'tpub-astrophysics-by-month2.md',
                     'tpub-astrophysics2.md',
                     'tpub-by-month2.md',
                     'tpub-exoplanets-by-month2.md',
                     'tpub-exoplanets2.md',
                     'tpub2.md']

file_change(filename_list_in,
                check_list,
                rep_list,
                filename_list_out)
