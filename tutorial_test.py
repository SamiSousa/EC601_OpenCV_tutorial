
import numpy as np
import cv2

#open an image

img = cv2.imread("img/coffee_context.jpg",1)

#cv2.imwrite('save_image.png', img)

cv2.namedWindow('Steph and coffee', cv2.WINDOW_AUTOSIZE | cv2.WINDOW_KEEPRATIO)
cv2.imshow('Steph and coffee', img)


#wait for the user to close the window
cv2.waitKey(0)

cv2.destroyAllWindows()
