import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('img/watch.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200, 300, 400], [100, 200, 300], 'c', linewidth=5)
plt.show()
