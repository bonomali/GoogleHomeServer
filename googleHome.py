# spoke something on GoogleHome
#
# use: ./ghome_say [ghome_ip] [text_to_say]
#
#

import sys
import pychromecast
import os
import os.path
from gtts import gTTS
import time
import hashlib

ip='192.168.1.15'
say='hey google play music'

#********* retrieve local ip of my rpi3
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip=s.getsockname()[0]
s.close()
#**********************
fname=hashlib.md5(say.encode()).hexdigest()+".mp3"; #create md5 filename for caching

castdevice = pychromecast.Chromecast(ip)
castdevice.wait()
vol_prec=castdevice.status.volume_level
castdevice.set_volume(0.0) #set volume 0 for not hear the BEEEP

fileDirectory = os.getcwd() + '/mp3_cache/'
filePath = fileDirectory + fname
print('fileDirectory')
print(fileDirectory)
print('filePath')
print(filePath)
try:
   os.mkdir(fileDirectory)
#    os.mkdir("/home/pi/mp3_cache/")
except:
   pass

# if not os.path.isfile(filePath):
if not os.path.isfile("/home/pi/googleHome/mp3_cache/"+fname):
   tts = gTTS(say)
   tts.save(filePath)
#    tts.save("/home/pi/mp3_cache/"+fname)

mc = castdevice.media_controller
print('localhost: **')
print("http://"+local_ip+":3001/mp3_cache")
mc.play_media("http://"+local_ip+":3001/mp3_cache", "audio/mp3")
# mc.play_media("http://"+local_ip+"/mp3_cache/"+fname, "audio/mp3")

mc.block_until_active()

mc.pause() #prepare audio and pause...

time.sleep(1)
castdevice.set_volume(vol_prec) #setting volume to precedent value
time.sleep(0.2)

mc.play() #play the mp3

while not mc.status.player_is_idle:
   time.sleep(0.5)

mc.stop()

castdevice.quit_app()
