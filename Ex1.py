'''
    Load and Display Image.
'''

import cv2

# Path of the image to load and display
img_path = "my_images/Ken.png"

# load the image using imread() function
# imread(img_path, format)

img_unchanged = cv2.imread(img_path, -1)    # cv2.IMREAD_UNCHANGED (< 0 )
img_grayscale = cv2.imread(img_path, 0)     # cv2.IMREAD_GRAYSCALE (= 0 )
img_color = cv2.imread(img_path, 1)         # cv2.IMREAD_COLOR (> 0 )

# Create a Window for displaying the Images
cv2.namedWindow("Display Window", cv2.WINDOW_AUTOSIZE)

# display the image and wait for a key to be pressed
cv2.imshow("Display Window", img_unchanged)
cv2.waitKey(0)

cv2.imshow("Display Window", img_grayscale)
cv2.waitKey(0)

cv2.imshow("Display Window", img_color)
cv2.waitKey(0)