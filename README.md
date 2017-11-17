# disinfo_image_analysis
image compassion 
By Gordon Duncan

Requirments
Skimage.measure 
numpy
open cv2

This script analysis picture looking for  duplicates and near 
duplicates pictures that are not pixel for pixel the same but close think captions on an image

the input is done throught .txt files with one line being the aboslut path of a picture
the ouput is the picture, the picture it messaured agaits it SSID and MSE separted by commas

Due to the large work load this script takes a random sample of available pictures
and compares the center pixels for a match
if it finds a match it cheecks that picture agaist all pictures

this program is also muti threaded

near the beginning of the script, you will hvae some constant you will need to file the most imporant being the 
a refrance to the txt which has the paths for the photos you want to look at