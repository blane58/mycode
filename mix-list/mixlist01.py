#!/usr/bin/env python3

mylist = [ "192.168.0.5", 5060, "UP" ]
# This line will print the first item in the list #
print("The first item in the list (IP): " + mylist[0] )
# This line will print the second item in the list #
print("The second item in the list (port): " + str(mylist[1]) )
# This line will print the third item in the list #
print("The last item in the list (state): " + mylist[2] )
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
print("When I ssh into IP addresses: " + new_list[3] + " or " + new_list[4] + ",  I am unable to ping ports: " + str(new_list[0]) + ", " + str(new_list[1]) + " or " + str(new_list[2]) + ".")
