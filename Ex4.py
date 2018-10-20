'''
    Image Operations
'''

import cv2 
import imutils
import numpy as np

# Path of the Image
img_path = "my_images/eto.jpg"

# Load the Image
img = cv2.imread(img_path)

# if the image is too big resize it
img = imutils.resize(img, width = 600)

# Convert the Image to GrayScale using cvtColor() function.
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel Operator (or Sobel Filter) is particullary used in Edge Detection Algorithms
# where it creates a new image which emphasises on edges.
#
# cv2.Sobel() calculates Image Derivates using the Sobel Operator + Gaussian Smoothing.
# cv2.Sobel(src_image, ddepth, dx, dy, ksize = 3)
#   dx and dy are the order of derivatice of x and y respectively 
#   ksize is the size of the kernel to use (default is 3) i.e 3 x 3 is used.
sobelx = cv2.Sobel(grey, cv2.CV_32F, 1, 0)  # dx = 1 and dy = 0

# Get the Minimum and Maximum Intensity value after Calculating Image Derivative
minVal, maxVal = np.amin(sobelx), np.amax(sobelx)

# cv2.convertScaleAbs is used to Scale the Image, Calculate a absolute value and Convert the result to 8-bit.
# Formula:
#   Result(Image) = Saturation / (|Src(Image) * alpha + beta|)
draw = cv2.convertScaleAbs(sobelx, alpha = 255.0/(maxVal - minVal), beta = -minVal * 255.0/(maxVal - minVal))

# Create two nameWindows to Display the Original Image and Resultant Image
cv2.namedWindow("Original Image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Sobel Image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Output Image", cv2.WINDOW_AUTOSIZE)

# Display the Images and wait for a key to pressed to terminate.
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Image", sobelx)
cv2.imshow("Output Image", draw)
cv2.waitKey(0)