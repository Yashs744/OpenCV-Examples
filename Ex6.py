'''
    Image Processing: Contrast and Brightness of an Image
'''

import numpy as np
import cv2
import imutils

# Path of the Image
img_path = "my_images/Eto.jpg"

# Load the Image
img = cv2.imread(img_path)
img = imutils.resize(img, width = 600)

# Accessing each pixel value in the image
# Image Processing is to preprocess a image and convert it into a suitable image or 
# in other words take a image (or multiple) image as n input and perform some operation to give output image (or images)
# Eg: Color Correction, Hue Adjustment, Constrast and Brightness Control

# Contrast and Brightness Adjustment falls under the Point Operators or Point Process that is 
# where each pixel of the input image is manipulated indepently of the neighbouring pixels.
# Formula:
#   g(x) = alpha * f(x) + beta  where,
#       alpha and beta are used to control contrast and brightness respectively.

(Height, Width, Channels) = img.shape

# Setting the Alpha and Beta or Variable to adjust Contrast and Brightness
alpha = 1.0
beta = 16.0

# New Image
output = np.zeros(img.shape, img.dtype)

# Manipulating each pixel of the input image
for j in range(0, Height):
    for i in range(0, Width):
        for k in range(0, Channels):
            output[j, i, k] = np.clip((alpha * img[j, i, k]) + beta, 0, 255)


# other way is to use the cv2.convertScaleAbs() function
# cv2.convertScaleAbs() Scales, Calculates the Absolute Value and 
# Convert the result to 8-bit type.

# Define a new array of all zeros (with shape and data type same as input image)
new_img = np.zeros(img.shape, img.dtype)
# Apply the function
new_img = cv2.convertScaleAbs(img, alpha = alpha, beta = beta)

# Display the Results.
cv2.imshow("Original Image", img)
cv2.imshow("Output Image 1", output)
cv2.imshow("Output Image 2", new_img)
cv2.waitKey(0)
