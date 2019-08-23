# This is one of my .py files
#!/usr/bin/env python3

import re
with open("cssophosts.txt", 'r') as req:
    for line in req:
        mymatch = re.search("^[a-z][a-z][a-z]cssopp0\d[a-z][a-z]\d\d\.vzbi\.com,\d+\.\d+\.\d+\.\d+,.+\s\d+,.+o", line)
        print(mymatch)
