# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Thu Jul 12 22:05:42 2018
# 
# @author: Asif Towheed
# """
# 
# from skimage.measure import compare_ssim
# import imutils
# import pyrealsense2 as rs
# import numpy as np
# from PIL import Image
# import cv2
# import time
# 
# # =============================================================================
# # t_end = time.time() + 60 * 15
# # while time.time() < t_end:
# # 
# # =============================================================================
# 
# def capture_image():
#     # Configure color stream
#     pipeline = rs.pipeline()
#     config = rs.config()
#     config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
#     
#     # Start streaming
#     pipeline.start(config)
#     
#     i = 0
#     t_end = time.time() + 5
#     while time.time() < t_end:
#         # Wait for frame: color
#         frame = pipeline.wait_for_frames()
#         color_frame = frame.get_color_frame()
#         
#         # Convert image to numpy arrays
#         color_image = np.asanyarray(color_frame.get_data())
#         
#         # Show image
#         cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
#         cv2.imshow('RealSense', color_image)
#         im.save("image-"+str(i)+".jpeg")
#         i += 1
#         cv2.waitKey(1)
#     pipeline.stop()
# #    return color_image
#     
# 
# for k in range(0,i - 1):
#     
# im = Image.fromarray(capture_image())
# t_end = time.time() + 5
# while time.time() < t_end:
#     print('')
# im = Image.fromarray(capture_image())
# im.save("image-2.jpeg")
# 
# imageA = cv2.imread("image-1.jpeg")
# imageB = cv2.imread("image-2.jpeg")
#  
# # convert the images to grayscale
# grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
# grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
# 
# # compute the Structural Similarity Index (SSIM) between the two
# # images, ensuring that the difference image is returned
# (score, diff) = compare_ssim(grayA, grayB, full=True)
# diff = (diff * 255).astype("uint8")
# print("SSIM: {}".format(score))
# 
# # threshold the difference image, followed by finding contours to
# # obtain the regions of the two input images that differ
# thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if imutils.is_cv2() else cnts[1]
# 
# # loop over the contours
# for c in cnts:
# 	# compute the bounding box of the contour and then draw the
# 	# bounding box on both input images to represent where the two
# 	# images differ
# 	(x, y, w, h) = cv2.boundingRect(c)
# 	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
# 	cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
#  
# # show the output images
# cv2.imshow("Original", imageA)
# cv2.imshow("Modified", imageB)
# cv2.imshow("Diff", diff)
# cv2.imshow("Thresh", thresh)
# cv2.waitKey(0)
# 
# 
# 
# 
# 
# =============================================================================


import cv2
import time

person_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml') # We load the cascade for the face.
cap = cv2.VideoCapture(0)
while True:
    r, frame = cap.read()

    start_time = time.time()
#    frame = cv2.resize(frame,(640,360)) # Downscale to improve frame rate
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # Haar-cascade classifier needs a grayscale image
    rects = person_cascade.detectMultiScale(gray_frame)
    
    end_time = time.time()
    print("Elapsed Time:",end_time-start_time)
            
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)
    cv2.imshow("preview", frame)
    k = cv2.waitKey(1)
    if k & 0xFF == ord("q"): # Exit condition
        break