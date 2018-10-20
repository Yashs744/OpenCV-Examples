'''
    Image Processing: Gamma Correction
'''

import numpy as np
import cv2
import imutils

# Path of the Image
img_path = "my_images/city_sky.jpg"

# Load the Image
img = cv2.imread(img_path)
img = imutils.resize(img, width = 600)

# Gamma Correction is a non-linear tranformation which is used to remove the
# non-linear mapping b/w input radiance and quantized pixel values.
# Formula:
#   g(x) = ((f(x) / 255.0) ^ gamma) * 255.0

# When γ < 1, 
#   the original dark regions will be brighter 
# When γ > 1,
#   the original bright region will be darker
gamma = 0.67

gamma_correction = np.array([(((i / 255) ** gamma) * 255.0) for i in range(0, 256)]).astype('uint8')

# Applying Gamma Correction to the Image using cv2.LUT() function
gamma_corrected_img = cv2.LUT(img, gamma_correction)

# Point Processes
point_operators_img = cv2.convertScaleAbs(img, alpha = 1.3, beta = 40)

# Display the Images
cv2.imshow("Original Image", img)
cv2.imshow("Point Processes Image", point_operators_img)
cv2.imshow("Gamma Corrected Image", gamma_corrected_img)
cv2.waitKey(0)