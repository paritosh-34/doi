from scholarLinks import google
from getdioLinks import doiLinks
from give_captcha_input import gci
from Extract_pdf_doi import pdf_doi

qs = input("Enter your Search query: ")
rg = int(input("How many pages of google would you like to search: "))

print("Searching ...")
Glinks = google(qs, rg)
print("Search Complete.")

print("Searching for dlinks ...")
dois = []
pdfs = []
for i in Glinks:
    print(i)
    d = doiLinks(i['url'])
    if d != "":
        if d.endswith("pdf"):
            pdfs.append(d)
        else:
            dois.append(d)

print("Done")

print("Writing")
with open('pdflist.txt', 'w') as filehandle:
    for listitem in pdfs:
        filehandle.write('%s\n' % listitem)

with open('doilist.txt', 'w') as filehandle:
    for listitem in dois:
        filehandle.write('%s\n' % listitem)

f = open("links.csv", "a")
for listitem in dois:
    f.write(listitem + ",\n")
f.close()

gci('links.csv', qs)

print('Searching for doi links in the downloaded pdfs ...')
pdfDois = pdf_doi(qs+'/')

f = open("pdflinks.csv", "a")
for listitem in pdfDois:
    f.write(listitem + ",\n")
f.close()

gci('pdflinks.csv', qs, style=False)