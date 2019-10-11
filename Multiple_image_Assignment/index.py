import numpy as np
import matplotlib.pylab as plt
import os
from PIL import Image, ImageOps

rootDir="./pic"
for dirName,subdirList,fileList in os.walk(rootDir):
    print('Found directory %s' % dirName)
    for fname in fileList:
          im= Image.open(fname)
          plt.imshow(im)
          print('\t%s'% fname)
