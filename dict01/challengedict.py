#!/usr/bin/env python3

hosts = [
        {"hostname": "North", "ip": "10.1.2.3"},
        {"hostname": "South", "ip": "10.4.5.6"},
        {"hostname": "West", "ip": "10.7.8.9"}
        ]


hosts.append ({"hostname": "East", "ip": "10.10.11.12"}) 

## display parts of the dictionary
#print( hosts )
#print( hosts[0]["hostname"], hosts[0]["ip"]) 
#print( hosts[1]["hostname"], hosts[1]["ip"]) 
#print( hosts[2]["hostname"], hosts[2]["ip"]) 
#print( hosts[3]["hostname"], hosts[3]["ip"]) 
for item in hosts:
    #print(item)
    #print(item["hostname"], item["ip"]) 
    print(f"The server {item["hostname"]} is using IP address: {item["ip"]}") 
