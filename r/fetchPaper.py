from scihub import SciHub
from datetime import datetime
sh = SciHub()
import csv

filename = 'links.csv'
with open(filename, 'rt') as csvfile: 
    csvreader = csv.reader(csvfile) 
    for row in csvreader: 
        try:
            toi = str(row[0])
            # print(toi)
            # toi = '10.1016/S0165-0114(99)00034-2'
            url = 'http://scihub.bban.top/'
            final = url + toi
            print(final)
            result = sh.fetch(final)

            with open('downloads/'+str(datetime.now())+'.pdf', 'wb+') as fd:
                fd.write(result['pdf'])
        except Exception as e:
            print(e)
