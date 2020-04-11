import cv2
import numpy as np
import matplotlib.pyplot as plt

# read image
img = cv2.imread("dbd.jpg")

# init ratio
alpha = 2.0
beta = -150
# new image
clear = alpha * img + beta
# limit min = 0 max = 255
clear = np.clip(clear, 0, 255)
# save image
cv2.imwrite("test.jpg", clear)
# just display results
# clear = cv2.cvtColor(clear, cv2.COLOR_BGR2RGB)
# img = plt.imshow(clear)
# plt.show()
