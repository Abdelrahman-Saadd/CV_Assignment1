import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Create a white background
img = np.ones((200, 550, 3), np.uint8) * 255

# Draw A
cv.line(img,(20,180),(90,20),(120,88,72),15)
cv.line(img,(90,20),(160,180),(120,88,72),15)
cv.line(img,(50,120),(130,120),(120,88,72),15)

# Draw D
cv.line(img,(200,180),(200,20),(120,88,72),15)

center_x = 200
center_y = 100
radius_width = 110
radius_height = 80

cv.ellipse(img, (center_x, center_y), (radius_width, radius_height), 0, 90, -90, (120,88,72), 15)

# Draw I
cv.line(img,(360,180),(360,20),(120,88,72),15)

# Draw B
cv.line(img,(420,180),(420,20),(120,88,72),15)

center_x1 = 420
center_y1 = 55
radius_width1 = 80
radius_height1 = 35
cv.ellipse(img, (center_x1, center_y1), (radius_width1, radius_height1), 0, 90, -90, (120,88,72), 15)

center_x2 = 420
center_y2 = 135
radius_width2 = 90
radius_height2 = 45
cv.ellipse(img, (center_x2, center_y2), (radius_width2, radius_height2), 0, 90, -90, (120,88,72), 15)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.axis('off')
plt.show()