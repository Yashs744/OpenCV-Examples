# OpenCV-Examples
Examples of OpenCV with Python

## 1. Basic Image Operation: Load and Display Image (Example 1)

- Load an Image in Memory using **_cv2.imread(image_path, format)_** function. Format take value of IMREADMODES. Avilable Modes to read an image are: **cv2.IMREAD_COLOR, cv2.IMREAD_UNCHANGED, cv2.IMREAD_GRAYSCALE, cv2.IMREAD_ANYCOLOR** etc.
- Display the Image Loaded using **_cv2.imshow(Message, image)_** function.
- After displaying the image wait for user to press a key to terminate. **_cv2.waitKey(0)_**

### Methods Used:
  - cv2.imread()
  - cv2.namedWindows()
  - cv2.imshow()
  - cv2.waitKey()
  
### Output:
![UnChanged Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_1(1).png)
![GrayScale Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_1(2).png)

## 2. Basic Image Operation: Tranforming (or Modifiying) Image i.e from BRG-to-GrayScale (Example 2)

- Modify the Image from BGR Channel to GrayScale Channel using **_cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)_**.
- Write the new Image to Disk using **_cv2.write(name, image)_**

### Methods Used:
  - cv2.cvtColor()
  - cv2.COLOR_BGR2GRAY
  - cv2.resize()
  - cv2.imwrite()

### Output:
![UnChanged Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_2.png)

## 3. Mask Operation on Image (Example 3)

- Enhance the Image by Manipulating each pixel using the formula<br>
    _pixel_value = 5 * IMG(j, i) - \[IMG(j - 1, i) + IMG(j + 1, i) + IMG(j, i - 1) + IMG(j, i + 1)_.
- Another way to enhance the image is correlating the Image with a Kernel using **_cv2.filter2D(img, ddpeth, kernel)_**.
<p align="center">
  <img src = "https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_phv%20%5Clarge%20kernel%20%3D%20%5Cbegin%7Bbmatrix%7D%200%26%20-1%26%200%5C%5C%20-1.5%26%205%26%20-1.5%5C%5C%200%26%20-1%26%200%20%5Cend%7Bbmatrix%7D">
</p>
 
  
### Methods Used:
  - Manual Manipulation of Pixels using NumPy
  - cv2.filter2D()
  
### Output:
![Original Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_3(1).png)
![Manual Manipulation Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_3(2).png)
![Filter2D Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_3(3).png)

## 4. Image Operation (Example 4)

### Methods Used:
  - cv2.cvtColor()
  - cv2.Sobel()
  - cv2.convertScaleAbs()
  
### Output:
![Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_4.png)

## 5. Blending Two Images (Example 5)

- Blend two Images together using Linear Blend i.e ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_phv%20%5Csmall%20g%28x%29%20%3D%20%281%20-%20%5Calpha%20%29f_1%28x%29%20&plus;%20%5Calpha%20f_2%28x%29)
- **_cv2.addWeigthed(array_1, alpha, array_2, beta, gamma)_** is used to blend the two images together (gamma = 0)

```shell
python (or python3) --image_1 "my_images/TG.jpg" --image_2 "my_images/TokyoGhoul.jpg"
```

### Methods Used:
  - cv2.addWeighted()
  
### Output:
![Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_5.png)

## 6. Image Processing: Contrast and Brightness

- Image Processing is to pre-process a image and convert it into a suitable image or in other words take a image (or multiple) image as n input and perform some operation to give output image (or images). <br>Example: Color Correction, Hue Adjustment, Contrast and Brightness Control.
- Point Operators (or Point Processes) is one of the Image Processing method where each pixel is manipulated independently from it's neighboring pixels. Formula:<br>
  <p align="center">
    <img src="https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cdpi%7B150%7D%20%5Cfn_cs%20g%28x%29%20%3D%20%5Calpha%20*%20f%28x%29%20&plus;%20%5Cbeta" alt="equation"/></p>
  where <i>alpha</i> and <i>beta</i> are used to control contrast and brightness respectively.

### Methods Used:
  - cv2.convertScaleAbs()
  - NumPy clip() for manual manipulation
  
### Output:
![Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_6.png)

### 7. Image Processing: Gamma Correction (Example 7)

- Gamma Correction is a non-linear tranformation which is used to remove the non-linear mapping b/w input radiance and quantized pixel values. Reference: [Computer Vision Algorithms and Applications by Richard Szeliski](http://szeliski.org/Book/)

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cdpi%7B200%7D%20%5Clarge%20g%28x%29%20%3D%20%5Cleft%20%28%20%5Cfrac%7Bf%28x%29%7D%7B255%7D%20%5Cright%20%29%5E%7B%5Cgamma%20%7D%20*%20255" alt="Formula">
</p>

### Methods Used:
  - NumPy Array
  - cv2.LUT()
  - cv2.convertScaleAbs()
  
### Output:
![Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_7.png)

### 8. Image Processing: Fetching Objects from Images based on Color (Example 8)

### Methods Used:
  - cv2.cvtColor()
  - np.uint8()
  - cv2.inRange()
  - cv2.GaussianBlur()
  - cv2.bitwise_and()
  
### Output:
![Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_8(1).png)
![Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_8(2).png)

### 9. Image Processing: Smoothing (or Bluring) an Image using Filters.

Smoothing or Bluring of an Image is a common task in Image Processing which is performed to reduce the noise from the image using filters. <br>
The most common type of filter is Linear Filter where output pixel's value is calculated using the weighted sum of the input pixel value.
		
<p align="center">
    <img src = "https://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20g%28i%2C%20j%29%20%3D%20%5Csum_%7Bk%2C%20l%7D%20f%28i%20&plus;%20k%2C%20j%20&plus;%20l%29h%28k%2C%20l%29" />
</p>

where, ![h(k,l)](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cdpi%7B120%7D%20h%28k%2C%20l%29) is a kernel which is nothing but the filter coefficients.

#### Types of Filters:
  - [Normalized Box Filter](https://en.wikipedia.org/wiki/Box_blur)

    ![box_filter](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cdpi%7B150%7D%20%5Cfn_cm%20%5Clarge%20K%20%3D%20%5Cfrac%7B1%7D%7BK_%7Bwidth%7D%20*%20K_%7Bheight%7D%7D%5Cbegin%7Bbmatrix%7D%201%26%201%26%20...%26%201%5C%5C%201%26%201%26%20...%26%201%5C%5C%20.%26%20.%26%20...%26%20.%5C%5C%20.%26%20.%26%20...%26%20.%5C%5C%201%26%201%26%201%26%201%20%5Cend%7Bbmatrix%7D)

    
    Here, each output pixel is the mean of the kernel neighbours. One such filter is _Box Blur_ or _Box Linear Filter_.
    
    ![box_blur](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cdpi%7B150%7D%20%5Cfn_cm%20%5Clarge%20K%20%3D%20%5Cfrac%7B1%7D%7B9%7D%5Cbegin%7Bbmatrix%7D%201%26%201%26%201%5C%5C%201%26%201%26%201%5C%5C%201%26%201%26%201%20%5Cend%7Bbmatrix%7D)
    
  - [Gaussian Filter](https://en.wikipedia.org/wiki/Gaussian_filter)<br>
    The Gaussian Filter works by convolving each pixel in the input image with a **_Gaussian Function_** and then summing them up together.
    
    [Gaussian Function](https://en.wikipedia.org/wiki/Gaussian_function):<br>
      ![1d](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Clarge%20g%28x%29%20%3D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B2%5Cpi%5Csigma%5E%7B2%7D%7D%7De%5E%7B-%5Cfrac%7Bx%5E%7B2%7D%7D%7B2%5Csigma%5E%7B2%7D%7D%7D) and 
      ![2D](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Clarge%20g%28x%29%20%3D%20%5Cfrac%7B1%7D%7B2%5Cpi%5Csigma%5E%7B2%7D%7De%5E%7B-%5Cfrac%7Bx%5E%7B2%7D%20&plus;%20y%5E%7B2%7D%7D%7B2%5Csigma%5E%7B2%7D%7D%7D)
      
  - [Median Filter](https://en.wikipedia.org/wiki/Median_filter)<br?
    It works by traversing through each pixel in the input image and replacing the pixel with the median of its neighbouting pixels.
    
  - [Bilateral Filter](https://en.wikipedia.org/wiki/Bilateral_filter)<br>
    It is an non-linear, edge-preserving and noise reducing filter i.e apart from reducing the noise from the image it also preserves the edges of the image i.e doesnot smooth out the edges rather replaces the intensity of each pixel with a weighted average of intensity value from the nearby pixels.
    
### Methods Used:
  - cv2.blur()
  - cv2.GaussianBlur()
  - cv2.medianBlur()
  - cv2.bilateralFilter()
  
### Output:
  ![output](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_9.png)


### 10. Morphological Image Processing

Morphological Image Processing is a collection of non-linear operations related to the shape of morphological features in the image. Morphological Operations usually works on Binary Images as it only rely on the relative ordering of pixel values and not on thier numerical values but they can also be applied to GreyScale Images.<br>
Morphological Operatations uses an <i>Structuring Element</i> which is nothing but a small binary image (matrix) of pixels each with a value of 0 or 1. This Structuing Element _(s)_ is applied to an input image _(f)_ to get a output _(g)_.

The two most common Morphological Operations are:
- Dilation
	The Operation consist of colvolving an image (f) with some structuring element (s). The Structuring Element (s) has a defined anchor point (or origin) which is usually at the center. As, (s) moves over the image (f), the maximum pixel overlapped by (s) is computed and the image pixel value is replaced by this maximum value. This operation _grows_ the bright region in the image.
	  	  
- Erosion
	Erosion is in a way opposite of Dilation as it calculates the minimum over the area of the given structuring element (s). It _shrinks_ the bright region in the image.
	
### Methods Used:
- cv2.getStructuringElement()
- cv2.erode()
- cv2.dilate()
- cv2.putText()
    
### Output:

   **_Structuring Element (s)_**: 
   	- **Shape**: cv2.MORPH_RECT
	- **Size**: (3, 3)
   
   ![result_10(rect)](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/result_10(rect).png)
   
   **_Structuring Element (s)_**: 
   	- **Shape**: cv2.MORPH_CROSS 
	- **Size**: (3, 3)
   
   ![result_10(rect)](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/result_10(cross).png)
   
   **_Structuring Element (s)_**: 
   	- **Shape**: cv2.MORPH_ELLIPSE
	- **Size**: (3, 3)
   
   ![result_10(rect)](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/result_10(ellipse).png)
   
	    
---
