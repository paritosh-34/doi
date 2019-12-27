import requests

r = requests.get('https://scholar.google.com/scholar?q=a')

print(r.text)

# import urllib.request
#
# r = urllib.request.urlopen('https://scholar.google.com/scholar?q=a')
#
# print("result code: " + str(r.getcode()))
#
# data = r.read()
# print(data)