import urllib.request, urllib.error, urllib.parse 

F = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in F: 
    print(line.decode().strip())
