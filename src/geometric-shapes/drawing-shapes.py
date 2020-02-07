import numpy as np
import cv2

img = cv2.imread('lena.jpg', 1)

# regualr line
img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 10)

# arrowed line
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 5)

# draw rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), -1)

# draw a circle
img = cv2.circle(img, (447, 64), 63, (0, 255, 0), -1)

# draw text
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

