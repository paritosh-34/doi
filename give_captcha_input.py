from scidownl.scihub import *
import csv


def gci(filename, output_directory):
    with open(filename, 'rt') as csvfile:
        csvreader = csv.reader(csvfile)
        counter = 1
        not_found = []
        for row in csvreader:
            try:
                print(row)
                sci = SciHub(str(row[0]), nom=counter, out=output_directory).download(choose_scihub_url_index=3)
            except Exception as e:
                print(e)
                not_found.append(counter)
                f = open("pdf_not_found_links.csv", "a")
                f.write(row[0] + ",\n")
            finally:
                counter += 1

    if len(not_found) != 0:
        print("These pdf were not found :-")
        print(not_found)
        print("Links in pdf_not_found_links.csv")
