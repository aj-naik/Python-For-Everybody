import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

sum = 0

comments = js['comments']
for items in comments:
    i = items['count']
    sum += int(i)

print("Count:"+str(len(comments)))
print("Sum"+str(sum))
