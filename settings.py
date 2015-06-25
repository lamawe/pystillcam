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

    settings = {'filetype' : 'jpg',
                'width' : resx['small'],
                'height' : resy['small'],
                'style' : sat['color'] }

    f = open(filename, 'w')
    pickle.dump(settings, f)
    f.close()            
    

if __name__ == "__main__":
    main(sys.argv)


