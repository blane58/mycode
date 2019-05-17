#!/usr/bin/env python3
import netifaces
for i in netifaces.interfaces():
     print('\n*************Details of Interface - ' + i + ' ****************')
     print('MAC address: '+ netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # Prints the MAC address
     print(' IP address: ' + netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # Prints the IP address
