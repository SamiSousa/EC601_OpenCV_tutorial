
import numpy as np
import cv2

import sys


if len(sys.argv) == 2:

	#provide path to image in command line

	img = cv2.imread(sys.argv[1])

	cv2.namedWindow( "Original image",  cv2.WINDOW_AUTOSIZE )
	cv2.imshow( "Original image", img)

	#split image into RGB channels
	BGR = cv2.split(img)

	cv2.imshow("Red",   BGR[2])
	cv2.imshow("Green",   BGR[1])
	cv2.imshow("Blue",   BGR[0])

	#print value at (20, 25)
	print("(20, 25) RGB:",img[20][25])


	ycrcb_image = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
	YCrCb = cv2.split(ycrcb_image)
	cv2.imshow("Y",   YCrCb[0])
	cv2.imshow("Cb",   YCrCb[1])
	cv2.imshow("Cr",   YCrCb[2])

	#print value at (20, 25)
	print("(20, 25) YCrCb:", ycrcb_image[20][25])

	hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	HSV = cv2.split(hsv_image)
	cv2.imshow("Hue",   HSV[0])
	cv2.imshow("Saturation",   HSV[1])
	cv2.imshow("Value",   HSV[2])

	#print value at (20, 25)
	print("(20, 25) HSV:",hsv_image[20][25])


	#wait for the user to close the window
	cv2.waitKey(0)

	cv2.destroyAllWindows()                                    


else:

	print("Usage: python ColorImage.py image_path.extension")

