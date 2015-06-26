#!/usr/bin/env python
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
   cam.ISO = r['ISO']
   cam.exposeure_mode = r['mode']
   cam.exposure_compensation = r['ev']
   cam.image_effect = r['effect']
   cam.exif_tags['IFD0.Copyright'] = r['rights']
   cam.exif_tags['EXIF.UserComment'] = r['comment']
   #cam.led = False

   print('Starting.') 
   for filename in cam.capture_continuous('pic/img{timestamp:%Y%m%d}{counter:03d}.jpg', format='jpeg'):
       print('Captured %s' % filename)
       print('Sutter speed: %s' % cam.exposure_speed)
       print cam.framerate
       print cam.exif_tags
       time.sleep(15) 
   
   
    
if __name__ == "__main__":
    main(sys.argv)
