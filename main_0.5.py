from scholarLinks import google
from getdioLinks import doiLinks

qs = input("Enter your Search query: ")

print("Searching ...")
Glinks = google(qs)
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

print(dois)
print(pdfs)