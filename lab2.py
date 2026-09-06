#LAP2
#Sarah Aljammaz

import numpy as np

img = np.arange(36).reshape(6, 6)
print("Original Image:\n", img)

center = img[1:5, 1:5]
print("\nCenter Region:\n", center)

bright_center = center + 10
print("\nBrightened Center:\n", bright_center)

img[1:5, 1:5] = bright_center
print("\nUpdated Image:\n", img)

print("\nMean Intensity:", img.mean())
print("Max Intensity:", img.max())
print("Min Intensity:", img.min())

img[0, :] -= 5
img[-1, :] -= 5
img[1:-1, 0] -= 5
img[1:-1, -1] -= 5

print("\nImage after border modification:\n", img)

print("\nFinal Standard Deviation:", img.std())
