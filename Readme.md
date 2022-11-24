# Traffic Light Identification Using OpenCV

## Prerequisites
- Python 3.6 and later
- Libraries - Numpy, OpenCV

## Approach
Since position of traffic light is fixed in used images, using image manipulation tools we can get pixel co-ordiantes of the traffic signal. Other approach would be to using object detctions algorithms to identify the traffic signals and iterate over objects to identify the color of signal. Another approach would be to idenitfy all circular objects with red,blue and amber color, recognizing color from circular object of interest.
    
Image is converted from BGR to HSV to create mask of colours(red, green, amber). On HSV color pallete, red pixels has two seprate range (at beginning and other at end), so creating two separte mask for both ranges or can create a combine mask. We will find amount of white pixels generated for particular color mask. Colour with more amount of white pixels after generating mask would be consider the color of traffic signal.

## Steps To Run
On terminal write command:
```python traffic_light_detection.py -i image_path```
