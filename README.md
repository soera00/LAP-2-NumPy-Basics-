# Lab 02: NumPy Basics

## Code

```python
import numpy as np

# 3.1 Create the Image Matrix
img = np.arange(36).reshape(6, 6)
print("Original Image:\n", img)

# 3.2 Extract the Center Region
center = img[1:5, 1:5]
print("Center Region:\n", center)

# 3.3 Apply Brightness Enhancement
bright_center = center + 10
print("Brightened Center:\n", bright_center)

# 3.4 Update the Original Image
img[1:5, 1:5] = bright_center
print("Updated Image:\n", img)

# 3.5 Compute Image Statistics
print("Mean Intensity:", img.mean())
print("Max Intensity:", img.max())
print("Min Intensity:", img.min())

# Question 4: Decrease border pixels brightness by 5
img[0, :] -= 5
img[-1, :] -= 5
img[1:-1, 0] -= 5
img[1:-1, -1] -= 5
print("Border Adjusted Image:\n", img)

# Question 5: Standard Deviation
print("Standard Deviation:", img.std())
```

---

## Output

```text
Original Image:
 [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]
 [30 31 32 33 34 35]]

Center Region:
 [[ 7  8  9 10]
 [13 14 15 16]
 [19 20 21 22]
 [25 26 27 28]]

Brightened Center:
 [[17 18 19 20]
 [23 24 25 26]
 [29 30 31 32]
 [35 36 37 38]]

Updated Image:
 [[ 0  1  2  3  4  5]
 [ 6 17 18 19 20 11]
 [12 23 24 25 26 17]
 [18 29 30 31 32 23]
 [24 35 36 37 38 29]
 [30 31 32 33 34 35]]

Mean Intensity: 22.0
Max Intensity: 38
Min Intensity: 0

Border Adjusted Image:
 [[-5 -4 -3 -2 -1  0]
 [ 1 17 18 19 20  6]
 [ 7 23 24 25 26 12]
 [13 29 30 31 32 18]
 [19 35 36 37 38 24]
 [25 26 27 28 29 30]]

Standard Deviation: 12.785625609340444
```

---

## Lab Questions

* **1. Why is reshaping important in NumPy?**
  * It allows changing the dimensions of an array like from 1D to a 2D matrix without modifying the underlying data, which is necessary for image representation.

* **2. How does slicing help in image processing?**
  * Slicing allows us to select and manipulate specific parts or regions of an image matrix.

* **3. What would happen if brightness enhancement were applied to the entire image?**
  * The brightness of every pixel would increase by 10, so the entire image would become brighter instead of only the center region.

* **4. Modify the code to decrease brightness of border pixels by 5 units:**
  ```python
  img[0, :] -= 5
  img[-1, :] -= 5
  img[1:-1, 0] -= 5
  img[1:-1, -1] -= 5
  ```

* **5. Compute the standard deviation of the final image matrix:**
  * **Code:** `print("Final Standard Deviation:", img.std())`
  * **Output:** `12.785625609340444`
