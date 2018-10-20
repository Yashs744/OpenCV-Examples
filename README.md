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
  where _alpha_ and _beta_ are used to control contrast and brightness respectively.

### Methods Used:
  - cv2.convertScaleAbs()
  - NumPy clip() for manual manipulation
  
### Output:
![Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_6.png)

### 7. Image Processing: Gamma Correction (Example 7)

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

## Execution
```shell
python (or python3) Ex1(or 2, 3, 4, 5, 6, 7, 8).py
```
