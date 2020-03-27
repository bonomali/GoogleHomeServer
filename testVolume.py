import sys
import pychromecast

ip='192.168.1.15'
vol=-1

try:
   vol=sys.argv[2]; #from 0 to 100
except:
   pass

castdevice = pychromecast.Chromecast(ip)
castdevice.wait()

if vol==-1 :
   vol_prec=castdevice.status.volume_level
   print(round(vol_prec*100))
else :
   castdevice.set_volume(float(vol)/100)
