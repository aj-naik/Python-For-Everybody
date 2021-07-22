import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

sum = 0
counts = tree.findall('.//count')
for items in counts:
    i = items.text
    sum += int(i)
print("Count:"+str(len(counts)))
print("Sum"+str(sum))
