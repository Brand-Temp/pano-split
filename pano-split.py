import cv2
import sys

# Check args
if len(sys.argv) != 3:
    print('Incorrect number of args, see readme.')
    exit(1)

pano = cv2.imread(sys.argv[1])
pano_height, pano_width, _ = pano.shape
num_splits = int(sys.argv[2])
split_offset = (pano_width % pano_height) / num_splits
split_width = pano_height + split_offset

for i in range(num_splits):
    print('Splitting %s into split_%d'%(sys.argv[1], i))
    start = int(i*split_width)
    end = int((i+1)*split_width)
    cv2.imwrite('split_%d'%i, pano[start:end])
