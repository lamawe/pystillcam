#
# Python Still Camera
#
# create a settings file with defalt values for the camera control program
#

import sys
import time
import pickle

def main(argv):

    filename = 'settings.txt'

    resx = {'small': 640, 'medium':1024, 'large': 1280, 'xtra-large':1600, 'full':2592}
    resy = {'small': 480, 'medium':768, 'large':1024, 'xtra-large':1200, 'full':1944}
    sat = {'color': 0, 'bw': -100, 'fx01': -50, 'vibrant': 100}

    sharpness = 0
    contrast = 0
    brightness = 50
    saturation = 0
    # ISO = 0
    ISO = 800
    video_stabilization = False
    exposure_compensation = 0

    # exposure_mode = 'auto'
    # exposure_mode = 'off'
    # exposure_mode = 'night'
    # exposure_mode = 'nightpreview'
    # exposure_mode = 'backlight'
    # exposure_mode = 'spotlight'
    exposure_mode = 'sports'
    # exposure_mode = 'snow'
    # exposure_mode = 'beach'
    # exposure_mode = 'verylong'
    # exposure_mode = 'fixedfps'
    # exposure_mode = 'antishake'
    # exposure_mode = 'fireworks'

    image_effect = 'none'
    # image_effect = 'negative'
    # image_effect = 'solarize'
    # image_effect = 'sketch'
    # image_effect = 'denoise'
    # image_effect = 'emboss'
    # image_effect = 'oilpaint'
    # image_effect = 'hatch'
    # image_effect = 'gpen'
    # image_effect = 'pastel'
    # image_effect = 'watercolor'
    # image_effect = 'film'
    # image_effect = 'blur'
    # image_effect = 'saturation'
    # image_effect = 'colorswap'
    # image_effect = 'washedout'
    # image_effect = 'posterise'
    # image_effect = 'colorpoint'
    # image_effect = 'colorbalance'
    # image_effect = 'cartoon'
    # image_effect = 'deinterlace1'
    # image_effect = 'deinterlace2'   
    
    meter_mode = 'average'
    # meter_mode = 'spot'
    # meter_mode = 'backlit'
    # meter_mode = 'matrix'

    #awb_mode = 'off'
    awb_mode = 'auto'
    # awb_mode = 'sunlight'
    # awb_mode = 'cloudy'
    # awb_mode = 'shade'
    # awb_mode = 'tungsten'
    # awb_mode = 'fluorescent'
    # awb_mode = 'incandescent'
    # awb_mode = 'flash'
    # awb_mode = 'horizon'
    
  
    color_effects = None

    rotation = 0
    hflip = False
    vflip = False
    crop = (0.0, 0.0, 1.0, 1.0)

    rights = 'Copyright (c) 2015 Wes LaMarche'
    comment = 'PI NoIR Camara'


    settings = {'filetype' : 'jpg',
                'width' : resx['small'],
                'height' : resy['small'],
                'style' : sat['color'],
                'ISO' : ISO,
                'ev' : exposure_compensation,
                'mode': exposure_mode,
                'effect' : image_effect,
                'rights' : rights,
                'comment' : comment }

    f = open(filename, 'w')
    pickle.dump(settings, f)
    f.close()            
    

if __name__ == "__main__":
    main(sys.argv)


