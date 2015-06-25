#
# Python Still Camera
#
# control program
#

import sys
import time
import pickle
import picamera

def main(argv):

   s = 'settings.txt'

   f = open(s, 'r')
   r = pickle.load(f)
   f.close()

   print r

   cam = picamera.PiCamera()
   cam.resolution = (r['width'], r['height'])
   cam.saturation = r['style']
   #cam.led = False

   print('Starting.') 
   for filename in cam.capture_continuous('pic/img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(15) 
   
   
    
if __name__ == "__main__":
    main(sys.argv)
