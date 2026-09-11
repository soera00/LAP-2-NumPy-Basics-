#LAP2
#Sarah Aljammaz-2250030227

import numpy as np

img = np.arange(36).reshape(6, 6)
print("Original Image:\n", img)

center = img[1:5, 1:5]
print("Center Region:\n", center)

bright_center = center + 10
print("Brightened Center:\n", bright_center)

img[1:5, 1:5] = bright_center
print("Updated Image:\n", img)

print("Mean Intensity:", img.mean())
print("Max Intensity:", img.max())
print("Min Intensity:", img.min())

img[0, :] -= 5
img[-1, :] -= 5
img[1:-1, 0] -= 5
img[1:-1, -1] -= 5
print("Border Adjusted Image:\n", img)

print("Standard Deviation:", img.std())iation:", img.std())
