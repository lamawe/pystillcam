#
# Python Still Camera
#
# control program
#

import sys
import time
import pickle

def main(argv):

   filename = 'settings.txt'

   f = open(filename, 'r')
   r = pickle.load(f)
   f.close()

   print r
    
if __name__ == "__main__":
    main(sys.argv)
