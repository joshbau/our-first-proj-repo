import socket
import sys
import schedule
import time
from datetime import datetime

def pscan():
    try:
        for port in range(1,1000 + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((hostIP, port))
            if result == 0:
                print ("\nScan completed on:", datetime.now(),"\nPort {}: Open".format(port))
        sock.close()

    except KeyboardInterrupt:
        print ("Exiting")
        sys.exit()

    except socket.gaierror:
        print ("Hostname not resolved. Exiting")
        sys.exit()

    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()

def redir():
    sys.stdout =open('PSresults.txt', 'at')
    pscan

#Set localhost as IP to be scanned.
host = "localhost"
hostIP = socket.gethostbyname(host)

#Print message notifying of scanning in process
print ("" * 60)
print ("Please wait, scanning remote host", hostIP)
print ("" *60)

#Check the date and time the scan was started
t1 = datetime.now()

#Checking time again
t2 = datetime.now()

#Calculate scan duration.
total = t2 - t1

#Printing the information on the screen
print ('Scan Completed in:', total)

#Task schedule
#Run portscanner.py every 12 hours.
schedule.every(12).hours.do(pscan)
schedule.every(12).hours.do(redir)

while True:

    schedule.run_pending()
    time.sleep(1)