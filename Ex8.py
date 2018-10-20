'''
	Image Processing: Fetching Objects from Images based on Color.
'''
import cv2
import numpy as np

# path of the image to load
img_path = 'my_images/Eto.jpg'

# load the image 
img = cv2.imread(img_path)

if img.shape[0] > 1000:
	img = cv2.resize(img, (1000, 600))
elif img.shape[1] > 1000:
	img = cv2.resize(img, (600, 800))
elif img.shape[1] > 100 and img.shape[0] == img.shape[1]:
	img = cv2.resize(img, (800, 800))

# Modify the image i.e tranform the image into HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def MaskedImage(colorValue):
	'''
		colorValue: list of BGR Value.
	'''

	# Define the array of BGR Color
	color = np.uint8([[colorValue]])
	# Convert and get HSV value of the defined BGR Color.
	hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

	# Define the range of color in HSV to use i.e
	# if an object of that color lies between the range
	# fetch that object
	# Formula:
	# 	lower = [HSV_Value - 10, 50 (or 100), 50 (or 100)] to
	# 	upper = [HSV_Value + 10, 255, 255]
	lower = np.array([hsv_color[0, 0, 0] - 10, 50, 50])
	upper = np.array([hsv_color[0, 0, 0] + 10, 255, 255])

	# cv2.inRange() function checks whether the elements of the 
	# input array lie b/w the element of the two arrays (lower and upper)
	return cv2.inRange(hsv_img, lower, upper)


# Get Mask for Red, Green and Blue
red_mask = MaskedImage(colorValue = [0, 0, 255])
blue_mask = MaskedImage(colorValue = [255, 0, 0])
green_mask = MaskedImage(colorValue = [0, 255, 0])

# Apply the Gaussian Blur to smooth out the image
mask = red_mask
mask = cv2.GaussianBlur(mask, (3, 3), 0)

# cv2.bitwise_and() function computes the bitwise conjuction b/w
# two arrays.
# Formula:
# 	result = src_1 & src_2
# Perform bitwise operation on the original image with the mask
# mask is a 8 bit-single channel that specifies elements of 
# the output array to be changed.
result = cv2.bitwise_and(img, img, mask = mask)

# Display Image
cv2.imshow("Original Image", img)
cv2.imshow("Masked Image", result)

cv2.waitKey(0)