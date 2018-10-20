'''
    Blending Two Images.
'''

import cv2
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-img_1", "--image_1", required=True, help="First Image for Blending")
ap.add_argument("-img_2", "--image_2", required=True, help="Second Image for BLending")
args = vars(ap.parse_args())

# Path of the two images to blend.
img1_path = args['image_1']
img2_path = args['image_2']

# Load the two Images.
img_1 = cv2.imread(img1_path)
img_2 = cv2.imread(img2_path)

# Here, we are performing Linear Blending which is nothing other then adding two images together
# Formula:
#   g(x) = beta * f0(x) + alpha * f1(x) where,
#       beta = 1 - alpha
#       f0(x) is the Array of first Image and f1(x) is the array of second Image

# cv2.addWeigthed() is a function which calculates the weigthed sum of two array using
#   result = array_1 * alpha + array_2 * beta + gamma

# addWeigthed() can be used to calculate the linear blend of Images.
# with the assumptation that both the Images must be of same size and same depth.

if img_1.shape[:2] != img_2.shape[:2]:
    size = (1000, 600)

    img_1 = cv2.resize(img_1, size)
    img_2 = cv2.resize(img_2, size)

# Value of Alpha, Beta and Gamma
alpha = 0.8
beta = 1 - alpha
gamma = 0.0

# Apply the function with the defined values and images.
blended_image = cv2.addWeighted(img_1, alpha, img_2, beta, gamma)

# Display the Image
cv2.imshow("Blended Image", blended_image)
cv2.waitKey(0)