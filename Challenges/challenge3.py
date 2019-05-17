#!/usr/bin/env python3
import netifaces
for i in netifaces.interfaces():
     print('\n*************Details of Interface - ' + i + ' ****************')
     print('MAC address: '+ netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # Prints the MAC address
     print(' IP address: ' + netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # Prints the IP address# This is one of my .py files
#!/usr/bin/env python3

# Thursday morning challenge
# Use this code
import random
thursday = []
for x in range(10000):
    thursday.append(random.randint(1, 600))

# Then create a FUNCTION that:
# 1. Uses if/elif/else statements to sort the 'thursday' integers (in a for loop)
#    into their appropriate TV packages list and prints the length (len()) of each:
#    Basic 1 - 20
#    Standard 1 - 50
#    Premium 1 - 100
#    Premium HD 101 - 200
#    Extras  201 - 600
# 2. Execute the function passing the 'thursday' list as an argument
# *** Bonus Points ***
# Have your function return the longest lengthed list of channels.

def SORT(chan):
    basic = []
    standard = []
    premium = []
    premiumHD = []
    extras  = []
    for x in chan:
        if x > 0 and x <= 20:
            basic.append(x)
        elif x > 0 and x <= 50:
            standard.append(x)
        elif x > 0 and x <= 100:
            premium.append(x)
        elif x > 100 and x <= 200:
            premiumHD.append(x)
        else:
            extras.append(x)


    print("The Basic package contains these channels:",  basic)
    print("The Standard package contains these channels:",  standard)
    print("The Premium package contains these channels:",  premium)
    print("The Premium HD package contains these channels:",  premiumHD)
    print("The Extras package contains these channels:",  extras)

    print("The Extras package contains:",  len(basic),"channels")
    print("The Premium HD package contains:",  len(standard),"channels")
    print("The Premium package contains:",  len(premium),"channels")
    print("The Standard package contains:",  len(premiumHD),"channels")
    print("The Basic package contains:",  len(extras),"channels")

    total = [len(basic), len(standard), len(premium), len(premiumHD), len(extras)]
    print(max(total), "....is the largest number of channels in any single package")


SORT(thursday)
