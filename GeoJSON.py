import urllib.request, urllib.error, urllib.parse
import json 

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True: 
    address = input("Enter Location: ")
    if len(address)<1: 
        print('invalid address')
        break

    url = serviceurl + urllib.parse.urlencode({'address':address})

    print('Retrieving',url)
    uh = urllib.request.urlopen(url)
    info = uh.read().decode()
    print('Retrieved', len(info), 'characters')

    try: 
        js = json.loads(info)
    except: 
        js = None

    if not js or 'status' not in js or js['status']!='OK':
        print('=====Retrieve Failed=====')
        print(info)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js["result"][0]['formatted_address']
    print(location)
