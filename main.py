import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Create a white background
img = np.ones((200, 550, 3), np.uint8) * 255

# Draw A
cv.line(img,(20,180),(90,20),(132, 50, 0),30)
cv.line(img,(90,20),(160,180),(132, 50, 0),30)
cv.line(img,(50,130),(130,130),(132, 50, 0),20)

# Draw D
cv.line(img,(210,180),(210,20),(132, 50, 0),30)

center_x = 210
center_y = 100
radius_width = 110
radius_height = 80

cv.ellipse(img, (center_x, center_y), (radius_width, radius_height), 0, 90, -90, (132, 50, 0), 30)

# Draw I
cv.line(img,(380,180),(380,20),(132, 50, 0),30)

# Draw B
cv.line(img,(435,180),(435,20),(132, 50, 0),30)

center_x1 = 440
center_y1 = 55
radius_width1 = 80
radius_height1 = 35
cv.ellipse(img, (center_x1, center_y1), (radius_width1, radius_height1), 0, 90, -90, (132, 50, 0), 30)

center_x2 = 440
center_y2 = 135
radius_width2 = 90
radius_height2 = 45
cv.ellipse(img, (center_x2, center_y2), (radius_width2, radius_height2), 0, 90, -90, (132, 50, 0), 30)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.axis('off')
plt.show()