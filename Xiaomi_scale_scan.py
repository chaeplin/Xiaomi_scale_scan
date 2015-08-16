# Xiaomi_scale_scan.py by chaeplin@gmail.com 
# based on SwitchDoc Labs's iBeacon-Scanner-
# https://github.com/switchdoclabs/iBeacon-Scanner-
 

# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys

import bluetooth._bluetooth as bluez

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	#print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

try:
	while True:
		returnedList = blescan.parse_events(sock, 1)
	        if len(returnedList) > 0:
			(mac, uuid, major, minor, txpower, rssi) = returnedList[0].split(',', 6)
			# change mac and uuid
			if mac == '88:0f:10:83:ca:5c' and uuid[0:22] == '01880f1083ca5c0d161d18':
				measunit = uuid[22:24]	
                		measured = int((uuid[26:28] + uuid[24:26]), 16) * 0.01
	   
				if measunit == '03' or measunit == 'a3' : unit = 'lbs' 
				if measunit == '12' or measunit == 'b2' : unit = 'jin'
				if measunit == '22' or measunit == 'a2' : unit = 'Kg' ;  measured = measured / 2
					
				print("measured : %s %s" % (measured, unit))
				
				# to compare previous measurement , use major and minor ( should be time of measurement)
	
except KeyboardInterrupt:
       sys.exit(1)
