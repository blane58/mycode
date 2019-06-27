#!/usr/bin/env python3

import urllib.request
import json
#Track the ISS
majortom= 'http://api.open-notify.org/astros.json'

#Call the webservice
groundctrl = urllib.request.urlopen(majortom)

#Put fileobject into helmet
helmet = groundctrl.read()

#Decode json to python data structure
helmetson = json.loads(helnet.decode('utf-8'))

# display our pythonic data
print("\n\nConverfted Python Data")
print(helmetson)

for person in people:
    # print name on the craft
    print(f"{person['name']} is on the {person['craft']}")
