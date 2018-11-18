# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 22:16:18 2018

@author: Asif Towheed
"""

import pyrealsense2 as rs
import numpy as np
import cv2
import time
from PIL import Image

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detect(gray, frame, k): # We create a function that takes as input the image in black and white (gray) and the original image (frame), and that will return the same image with the detector rectangles. 
    rects, weights = hog.detectMultiScale(gray)
    for i, (x, y, w, h) in enumerate(rects): # For each detected face:
        if weights[i] < 0.7:
            continue
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # We paint a rectangle around the face.
        #frame = cv2.cvtColor(np.array(frame), cv2.COLOR_BGR2RGB)
        
        person = frame[y:y+h, x:x+w]
        pilimg = Image.fromarray(person)
        pilimg.save('person-{}.jpeg'.format(k))

    return frame # We return the image with the detector rectangles.


# Configure color stream
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

# =============================================================================
t_end = time.time() + 5
while time.time() < t_end:
    dumm = 0
# 
# =============================================================================
# =============================================================================
# # Wait for frame: color
# frame = pipeline.wait_for_frames()
# color_frame = frame.get_color_frame()
# 
# # Convert image to numpy arrays
# color_image = np.asanyarray(color_frame.get_data())
# 
# gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY) # We do some colour transformations.
# canvas = detect(gray, color_image) # We get the output of our detect function.
# 
# #canvas = cv2.cvtColor(np.array(canvas), cv2.COLOR_BGR2RGB)
# # Show image
# cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('RealSense', canvas)
# im = Image.fromarray(canvas)
# im.save("your_file.jpeg")
# pipeline.stop()
# cv2.waitKey(0)
# 
# =============================================================================

i = 0
k = 5
t_end = time.time() + 6
while time.time() < t_end:
    frame = pipeline.wait_for_frames()
    if frame is not None:
        print(i)
        i += 1
    if i%5 is 0:
        #======================================================================
        
        color_frame = frame.get_color_frame()

        # Convert image to numpy arrays
        color_image = np.asanyarray(color_frame.get_data())
        
        gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY) # We do some colour transformations.
        canvas = detect(gray, color_image, i) # We get the output of our detect function.
        
        #canvas = cv2.cvtColor(np.array(canvas), cv2.COLOR_BGR2RGB)
        # Show image
        #cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        #cv2.imshow('RealSense', canvas)
        im = Image.fromarray(canvas)
        im.save("your_file{}.jpeg".format(i))
        #pipeline.stop()
        #cv2.waitKey(0)

##        print("ho gaya")
        #======================================================================
##
##    if t_end - time.time() < k:
##        print("k changed")
##        k -= 1

