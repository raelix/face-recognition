import datetime
import sys
import os
import dlib
import glob
from skimage import io
import time

DEFAULT_SLEEP=0.1
DEFAULT_DIR="unknown_faces"


def main():
    if len(sys.argv) < 1:
        print('Please provide an URL or an image file')
    else:
        create_dir(DEFAULT_DIR)
        detect_face(DEFAULT_DIR, sys.argv[1], DEFAULT_SLEEP)

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def detect_face(dst_dir, src_img, time_sleep):
    detector = dlib.get_frontal_face_detector()
    while True:
        img = io.imread(src_img)
        dets = detector(img, 1)
        if len(dets) > 0:
            write_file(dst_dir, img)
        else:
            pass
        time.sleep(time_sleep)

def write_file(dst_dir, img):
    filename = '%s/%s.jpg' % (dst_dir, datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S'))
    try:
        io.imsave(filename, img)
    except:
        print('Exception writing image to file: %s' % filename)

if __name__ == '__main__':
    main()
