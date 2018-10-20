'''
    Load, Modify (Transform Color Image to GrayScale) and Save an Image.
'''

import cv2

# path of the image to load
img_path = 'my_images/Halloween.png'

# load the image 
original_img = cv2.imread(img_path)
original_img = cv2.resize(original_img, (800, 800))

# Modify the image i.e tranform the image into grayscale
# cvtColor(src_img, dst_img, tranformation)
# tranformation - cv2.COLOR_BGR2GRAY
grayscale_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

# Create a window to display images
cv2.namedWindow("Original Image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Transformed Image", cv2.WINDOW_AUTOSIZE)

# Display Image
cv2.imshow("Original Image", original_img)
cv2.imshow("Transformed Image", grayscale_img)

cv2.waitKey(0)

# Save the GrayScale Image
cv2.imwrite("../images/gray.png", grayscale_img)