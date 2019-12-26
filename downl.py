from scidownl.scihub import *
import csv

filename = 'links.csv'
with open(filename, 'rt') as csvfile: 
    csvreader = csv.reader(csvfile) 
    for row in csvreader: 
        try:
            out = 'paper'
            sci = SciHub(str(row[0]), out).download(choose_scihub_url_index=3)
        except Exception as e:
            print(e)


# from scidownl.scihub import *

# DOI = "10.1021/ol9910114"
# out = 'paper'
# sci = SciHub(DOI, out).download(choose_scihub_url_index=3)