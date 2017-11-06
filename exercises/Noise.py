
import numpy as np
from cv2 import *

import sys

def Add_salt_pepper_Noise(srcArr, pa, pb ):

	amount1=srcArr.shape[0]*srcArr.shape[1]*pa #Need to run through all channels
	amount2=srcArr.shape[0]*srcArr.shape[1]*pb
	for counter in range(0, int(amount1)):
	
		srcArr[int(np.random.uniform( 0,srcArr.shape[0]))][int(np.random.uniform(0, srcArr.shape[1]))] = 0

	
	for counter in range(0, int(amount2)):
	
		srcArr[int(np.random.uniform( 0,srcArr.shape[0]))][int(np.random.uniform(0, srcArr.shape[1]))] = 255
	



def Add_gaussian_Noise(srcArr, mean, sigma):

	dimensions = srcArr.shape
	gaussian = np.random.normal(mean,sigma, dimensions)

	for r in range(0, dimensions[0]):
		for c in range(0, dimensions[1]):
			srcArr[r][c] = srcArr[r][c] + gaussian[r][c]  #add noise to image
	return srcArr



if len(sys.argv) == 2:

	image = imread(sys.argv[1], 0)
	namedWindow( "Original image", WINDOW_AUTOSIZE )
	imshow( "Original image", image)

	kernel = (7,7)

	noise_img = image.copy()
	mean = 50
	sigma = 20		#Not the variance
	noise_img = Add_gaussian_Noise(noise_img, mean, sigma)
	imshow( "Gaussian Noise", noise_img)

	noise_dst = noise_img.copy()
	noise_dst = blur(noise_dst,kernel)	#3x3 kernel
	imshow( "Box filter", noise_dst)

	noise_dst1 = noise_img.copy()
	noise_dst1 = GaussianBlur(noise_dst1, kernel,1.5)
	imshow( "Gaussian filter", noise_dst1)

	noise_dst2 = noise_img.copy()
	noise_dst2 = medianBlur(noise_dst2,3)
	imshow( "Median filter", noise_dst2)

	#wait for the user to close the window
	waitKey(5000)	#wait only 5 seconds

	noise_img2 = image.copy()
	pa=0.4
	pb=0.4
	Add_salt_pepper_Noise(noise_img2, pa, pb)
	imshow( "Salt and Pepper Noise", noise_img2)

	noise_dst3 = noise_img2.copy()
	noise_dst3 = blur(noise_dst3,kernel)
	imshow( "Box filter", noise_dst3)

	noise_dst4 = noise_img2.copy()
	noise_dst4 = GaussianBlur(noise_dst4,kernel,1.5)
	imshow( "Gaussian filter", noise_dst4)

	noise_dst5 = noise_img2.copy()
	noise_dst5 = medianBlur(noise_dst5,3)
	imshow( "Median filter", noise_dst5)

	#wait for the user to close the window
	waitKey(5000) #wait 5 seconds

	destroyAllWindows()  

else:

	print("Usage: python Noise.py image_path.extension")

