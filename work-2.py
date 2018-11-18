# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:40:19 2018

@author: Asif Towheed
"""

import cv2
import numpy as np
from PIL import Image
from PIL import ImageDraw

sum_w = sum_h = 0

for i in range(0,9):
    ori = cv2.imread("person-{}.jpeg".format(80 + i*5))
    if ori is not None:
        height, width, depth = ori.shape
        print("indw",width,"indh",height)
        sum_w += width
        sum_h += height
        print("w",sum_w,"h",sum_h)
    
final_w, final_h = sum_w/9, sum_h/9

for i in range(0,9):
    ori = cv2.imread("person-{}.jpeg".format(80 + i*5))
    newimg = cv2.resize(ori,(int(final_w),int(final_h)))
    pilimg = Image.fromarray(newimg)
    pilimg.save('new_person-{}.jpeg'.format(80 + i*5))


image1 = cv2.imread("new_person-85.jpeg")
image2 = cv2.imread("new_person-90.jpeg")


#image1 = Image.fromarray(image1)
#image2 = Image.fromarray(image2)
#image1 = np.asanyarray(image1.getdata())
#image2 = np.asanyarray(image2.getdata())

#image1 = np.array(image1.getdata())
#image2 = np.array(image2.getdata())

alpha = 0.5
imnew = cv2.addWeighted(image1,alpha,image2,alpha,0)
#result = Image.blend(image1, image2, alpha=0.5)
#result = image1 * (1.0 - alpha) + image2 * alpha

while(1):
    cv2.imshow("imnew", imnew)
    if cv2.waitKey(1) & 0xFF == ord('q'): # If we type on the keyboard:
        break # We stop the loop.

cv2.destroyAllWindows()







