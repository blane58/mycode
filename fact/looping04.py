#!/usr/bin/env python3
# Open file in "append mode
dnsfile3 = open("dnsservers.txt", "a")
my_words = input("What do you want to write?\n")
dnsfile3.write(my_words)
dnsfile3.close()
