# OpenCV-Examples
Examples of OpenCV with Python

## 1. Basic Image Operation: Load and Display Image (Example 1)

### Methods Used:
  - cv2.imread()
  - cv2.namedWindows()
  - cv2.imshow()
  - cv2.waitKey()
  
### Output:
![UnChanged Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_1(1).png)
![GrayScale Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_1(2).png)

## 2. Basic Image Operation: Tranforming (or Modifiying) Image i.e from BRG-to-GrayScale (Example 2)

### Methods Used:
  - cv2.cvtColor()
  - cv2.COLOR_BGR2GRAY
  - cv2.imwrite()

### Output:
![UnChanged Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_2.png)

## 3. Mask Operation on Image (Example 3)

### Methods Used:
  - Manul Manipulation of Pixels using NumPy
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
```shell
python (or python3) --image_1 "my_images/TG.jpg" --image_2 "my_images/TokyoGhoul.jpg"
```

### Methods Used:
  - cv2.addWeighted()
  
### Output:
![Image](https://github.com/Yashs744/OpenCV-Examples/blob/master/my_images/Output/result_5.png)

## 6. Image Processing: Contrast and Brightness

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
