import os
from time import gmtime, strftime


hora = strftime("%Y-%m-%d %H:%M:%S", gmtime())

print ""
print "[+] Raspberry Pi iniciada a las:  %s" % (hora)
print ""
os.system("omxplayer -p -o hdmi /home/pi/VideoHD/sunset.mp4")

