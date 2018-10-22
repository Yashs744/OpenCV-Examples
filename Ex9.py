'''
	Image Processing: Smoothing (or Bluring) an Image using Filters.
'''

import cv2
import imutils
import argparse
import numpy as np

# Initialize the Argument Parse and define the argument for the Image Path.
ap = argparse.ArgumentParser()
ap.add_argument("-img", "--image", help = "Path of the Image", default = "my_images/Eto.jpg")
args = vars(ap.parse_args())

# Load in the Image
img = cv2.imread(args['image'])
img = imutils.resize(img, width = 600)


# Size of the Kernel to use.
ksize = 3

# cv2.blur(src, ksize) Blurs an Image using the Normalized Box Filter.
box_blur = cv2.blur(img, ksize = (ksize, ksize))

# cv2.GaussianBlur(src, ksize, sigmaX, sigmaY) Blurs the Image using the Gaussian Filer.
# sigmaX and sigmaY are the Standard Deviation in X and Y direction respectively.
gaussian_blur = cv2.GaussianBlur(img, (ksize, ksize), 0)

# cv2.medianBlur(src, ksize) Blurs an Image using the Median Filter.
# ksize must be odd and greater than 1 (example: 3, 5, 7, 9, 11 ... )
median_blur = cv2.medianBlur(img, ksize = ksize)

# cv2.bilateralFilter(src, d, sigma_color, sigma_space) - Applies an Bilateral Filter to an Image.
# d: diameter of each pixel neighbourhood
# sigma_color = Standard Deviation in Color Space
# sigma_space = Standard Deviation in Coordinate Space.
bilateral_filter = cv2.bilateralFilter(img, ksize, ksize * 2, ksize / 2)


# Display Images
delay = 10

cv2.imshow("Original Image", img)
cv2.imshow("Box Blur", box_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)
cv2.imshow("Bilateral Filter", bilateral_filter)

cv2.waitKey(0)