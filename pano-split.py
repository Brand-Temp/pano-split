import cv2
import numpy as np
import sys

# Check args
if len(sys.argv) != 3:
    print('Incorrect number of args, see readme.')
    exit(1)

pano = cv2.imread(sys.argv[1])
pano_height, pano_width, _ = pano.shape
num_splits = int(sys.argv[2])
split_width = int(pano_width/num_splits)
splits = np.array_split(pano,3,1)
for i in range(num_splits):
    cv2.imwrite('split_%d.jpg'%i, splits[i])
