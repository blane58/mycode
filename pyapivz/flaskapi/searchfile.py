# This is one of my .py files
#!/usr/bin/env python3

import re
with open("cssophosts.txt", 'r') as req:
    for line in req:
        mymatch = re.search("^...cssopp0\d.+?.vzbi.com,\d+.\d+.\d+.\d+,.+,\s", line)
        print(mymatch)
