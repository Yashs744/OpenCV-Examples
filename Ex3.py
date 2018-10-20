# Mask Operation on an Image

import numpy as np
import cv2
import imutils

# Image Contrast Enhancement
def enhanceImage(original_image, format):
    '''
        Enchance the Image using the Formula mentioned below.
        Formula: 
            value = 5 * IMG(j, i) - [IMG(j - 1, i) + IMG(j + 1, i) + IMG(j, i - 1) + IMG(j, i + 1)]

        if the value is greater than 255 then
            IMG(j, i) = 255
        if the value is less than 0 then
            IMG(j, i) = 0

        Parameters:
            original_image: Original Image.
            format: Whether the image is GrayScale (0) or Colored (1)
    '''

    assert format in [0, 1], "Format for GrayScale is 0 and Colored is 1"

    # Get Height and Width of the Image
    if format == 0:
        (height, width) = original_image.shape

    if format == 1:
        #original_image = cv2.cvtColor(original_image, cv2.CV_8U)
        (height, width, channels) = original_image.shape

    # Enhanced Image
    new_image = np.zeros(original_image.shape, original_image.dtype)

    # Enchaned the Image using the Formula
    for j in range(1, height - 1):
        for i in range(1, width - 1):
            # For GrayScale Images
            if format == 0:
                value = 5 * original_image[j, i] - (original_image[j-1, i] + original_image[j+1, i] + original_image[j, i-1] + original_image[j, i+1])
                if value > 255:
                    new_image[j, i] = 255
                if value < 0:
                    new_image[j, i] = 0
            # For Colored Images
            if format == 1:
                for k in range(0, channels):
                    value = 5 * original_image[j, i, k] - (original_image[j-1, i, k] + original_image[j+1, i, k] + original_image[j, i-1, k] + original_image[j, i+1, k])
                    if value > 255:
                        new_image[j, i, k] = 255
                    if value < 0:
                        new_image[j, i, k] = 0

    return new_image
     
# Path of the Image to work-on
img_path = "my_images/Eto.jpg"

# Load the Image in GrayScale Mode
img = cv2.imread(img_path)
img = imutils.resize(img, width = 600)  # resize the image

# Output image

# Manually Operation
output = enhanceImage(img, 1)

# cv2.filter2D() convoles an image with the given kernel. It applies an arbitary
# linear kernel filter to the image. The function actually performs correlation rather
# than convolution.
# Formula:
#   IMG(x, y) = ∑(0≤y′<kernel.rows; 0≤x′<kernel.cols) kernel(x′,y′) * SRC_IMG(x + x′ − anchor.x, y + y′ − anchor.y)

# Define the Kernel to use for Enhance the Image.
kernel = np.array([[0, -1, 0], [-1.5, 5, -1.5], [0, -1, 0]], dtype = np.float32)
# Apply cv2.filter2D() function on the image with defined kernel
output_ = cv2.filter2D(img, -1, kernel)  # -1 is for ddpeth i.e output image have same depth as input
       
# Display the Images
cv2.imshow("Original Image", img)
cv2.imshow("Manual Enchaned Image", output)
cv2.imshow("Automatic Enchaned Image", output_)
cv2.waitKey(0)