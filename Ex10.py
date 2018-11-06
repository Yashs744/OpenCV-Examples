'''
    Morphological Image Processing - Dilation and Erosion
'''

import cv2
import imutils
import argparse
import numpy as np

# Initialize the Argument Parse and define the argument for the Image Path.
ap = argparse.ArgumentParser()
ap.add_argument("-img", "--image", help = "Path of the Image", default = "my_images/Eto.jpg")
args = vars(ap.parse_args())

# Load the Image
image = cv2.imread(args['image'])
image = imutils.resize(image, width = 600)

# Get Height of the Image
height = image.shape[0]

# Get Structuring Element
# Available Shapes: cv2. cv2.MORPH_RECT, cv2.MORPH_CROSS, cv2.MORPH_ELLIPSE
element_shape = cv2.MORPH_CROSS
element_size = (3,3)
text = f"Kernel Size: {element_size}"

# cv2.getStructuringElement(shape, ksize, anchor = (-1, -1))    # (-1, -1) implies the center
element = cv2.getStructuringElement(element_shape, element_size)

# Dilatation
# cv2.dilate(source_image, kernel)
dilated_image = cv2.dilate(image, element)

# Erosion
# cv2.erode(source_image, kernel)
eroded_image = cv2.erode(image, element)

# Add Text to the Output Image.
cv2.putText(dilated_image, text, (10, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
cv2.putText(eroded_image, text, (10, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

# Display the Original and Output Images.
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated_image)
cv2.imshow("Eroded Image", eroded_image)
cv2.waitKey(0)