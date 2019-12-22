from scholarLinks import google
from getdioLinks import doiLinks

qs = input("Enter your Search query: ")

print("Searching ...")
Glinks = google(qs)
print("Search Complete.")

print("Searching for dlinks ...")
dois = []
for i in Glinks:
    print(i)
    d = doiLinks(i['url'])
    if d != "":
        dois.append(d)

print("Done")
print(dois)