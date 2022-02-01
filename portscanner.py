#! /bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2 :
    target = socket.gethostbyname(sys.argv[1]) # translate hostname to IPv4
else:
    print("Invalid amout of arguments")
    print("Synatax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" *  50)
print("Scanning target..."+target)
print("Time started: "+str(datetime.now()))

try:    
    for port in range(20,90):
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target , port)) # an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting program...")
    sys.exit()

except socket.gaierror:
    print("Hostnme could not be resolved")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()