#!/usr/bin/env python
# Python Still Camera
#
# control program
#

import sys
import time
import pickle
import picamera

def log(msg):
   print time.strftime("%Y-%m-%d %H:%M:%S | ") + msg

def main(argv):

   s = 'settings.txt'

   f = open(s, 'r')
   r = pickle.load(f)
   f.close()

   log('Initialiing.')
   log(str(r))

   i = 1;
   while True:
       cam = picamera.PiCamera()
       cam.resolution = (r['width'], r['height'])
       cam.saturation = r['style']
       cam.ISO = r['ISO']
       cam.exposeure_mode = r['mode']
       cam.exposure_compensation = r['ev']
       cam.image_effect = r['effect']
       cam.exif_tags['IFD0.Copyright'] = r['rights']
       cam.exif_tags['EXIF.UserComment'] = r['comment']
       time.sleep(1) # Camera warm-up time
       filename = 'pic/img%03d.jpg' % i
       cam.capture(filename)
       cam.close()
       log(str('Captured %s' % filename))
       i += 1
       time.sleep(4) # Take approximately a picture per minue
       

'''   for filename in cam.capture_continuous('pic/img{timestamp:%Y%m%d}{counter:03d}.jpg', format='jpeg'):
       print('Captured %s' % filename)
       print('Sutter speed: %s' % cam.exposure_speed)
       print cam.framerate
       print cam.exif_tags
       time.sleep(15) '''
    
if __name__ == "__main__":
    main(sys.argv)
