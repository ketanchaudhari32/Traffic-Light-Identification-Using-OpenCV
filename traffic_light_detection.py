#importing libraries
import os
import numpy as np
import cv2
import argparse

#function to identify color of signal based on mask generated
def detect_main_color(hsv_image):

    # mapping colour names to HSV range
    #Since red color has two seprate ranges (at starting  and ending) on HSV pallete. 
    #Setting two different Upper and Lower range nask range for Red.
    colors = [
        ['red', [0,100,100], [10,255,255]], 
        ['red', [160,100,100], [180,255,255]], 
        ['amber', [88,100,100], [108,255,255]],
        ['green', [40, 50, 50], [90, 255, 255]],
    ]

    color_found = 'unknown'
    max_count = 0

    for color_name, lower_val, upper_val in colors:
        # threshold the HSV image - any matching color will show up as white
        mask = cv2.inRange(hsv_image, np.array(lower_val), np.array(upper_val))

        # count white pixels on mask
        count = np.sum(mask)
        if count > max_count:
            color_found = color_name
            max_count = count

    return color_found


if __name__=='__main__':

    #creating argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="filename", required=True, help="input file", metavar="FILE")
    args = parser.parse_args()

    #getting the file path
    file_path = args.filename

    #check if file path exist
    if os.path.exists(file_path):
        img = cv2.imread(file_path)

        #since location of traffic signal is fixed
        #Using Pixel value for location of traffic signal in image
        traffic_sign = img[55:95,285:305] 
        hsv = cv2.cvtColor(traffic_sign, cv2.COLOR_BGR2HSV)
        print(f"{file_path} - Traffic Sign : {detect_main_color(hsv)}")

    else:
        print('Invalid Path Provided')