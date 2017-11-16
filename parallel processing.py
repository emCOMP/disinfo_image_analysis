
# Windows bitmaps - *.bmp, *.dib (always supported)
#JPEG files - *.jpeg, *.jpg, *.jpe (see the Notes section)
#JPEG 2000 files - *.jp2 (see the Notes section)
#Portable Network Graphics - *.png (see the Notes section)
#WebP - *.webp (see the Notes section)
#Portable image format - *.pbm, *.pgm, *.ppm (always supported)
#Sun rasters - *.sr, *.ras (always supported)
#TIFF files - *.tiff, *.tif (see the Notes section)
# file types that should work for comparsion
from skimage.measure import compare_ssim as ssim
import numpy as np
import cv2
import sys
import random
from multiprocessing import Pool
sampleSize = 100
def dupChecker(input1):
    stdout = open('output9.txt','a')
    stdin = open(input1,'r')
    lines = stdin.readlines()
    match = False
    for x in range(0,len(lines)-1):
            original = cv2.imread(lines[x].rstrip(),1)
            # takes a random saple of sampleSize photos to compare agaist the base
            for z in range(sampleSize):
                            ran = random.randrange(len(lines))
                            while(ran == x):
                                    ran = random.randrange(len(lines))
                            original = cv2.imread(lines[x].rstrip(),1)
                            contrast = cv2.imread(lines[ran].rstrip(),1)
                            if(original is not None and contrast is not None):
                                    original = cv2.imread(lines[x].rstrip(),1)
                                    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
                                    contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
                                    original = cv2.resize(original, (700,700))
                                    contrast = cv2.resize(contrast, (700,700))
                                    shopped1 = original[250:450,250:450]
                                    shopped2 = contrast[250:450,250:450]
                                    m = mse(shopped1,shopped2)
                                    if(lines[x]!= lines[ran]):
                                       if(m <= 500):
                                            match = True
                                            
            if(match is True):
                    # if a match is found check ever image and print all images with ssim above .8 and MSE bellow 500
                    for y in range(x,len(lines)-1):
                            contrast = cv2.imread(lines[y+1].rstrip(),1)
                            if(lines[x] != lines[y+1]):
                                    if(original is not None and contrast is not None):
                                            original = cv2.imread(lines[x].rstrip(),1)
                                            original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
                                            contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
                                            original = cv2.resize(original, (700,700))
                                            contrast = cv2.resize(contrast, (700,700))
                                            compare_images(original, contrast, "",x,y,stdout,lines)
                    match is False
                            
                                                               
    stdout.close()
    stdin.close()
    return True

def mse(imageA, imageB):
        # the 'Mean Squared Error' between the two images is the
        # sum of the squared difference between the two images;
        # NOTE: the two images must have the same dimension
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        
        # return the MSE, the lower the error, the more "similar"
        # the two images are
        return err

def compare_images(imageA, imageB, title,x,y,stdout,lines):
        # compute the mean squared error and structural similarity
        # index for the images
        m = mse(imageA, imageB)
        if(m<=500):
                s = ssim(imageA, imageB)
                if(s >= .8):
                        stdout.write(lines[x].rstrip() + " vs " + lines[y+1].rstrip()+ ", ")
                        stdout.write("MSE: %.2f, SSIM: %.2f,\n" % (m, s))
                        stdout.write("\n")
        

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(dupChecker, ['txt/list70-80kb.txt', 'txt/list80-90kb.txt', 'txt/list90-100kb.txt','txt/list60-70kb.txt']))
        

