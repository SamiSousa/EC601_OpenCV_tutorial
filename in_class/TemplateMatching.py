import numpy as np
import cv2

def TemplateMatching(src, temp, stepsize): # src: source image, temp: template image, stepsize: the step size for sliding the template
    mean_t = 0;
    var_t = 0;
    location = [0, 0];

    correlations = {}
    # Calculate the mean and variance of template pixel values
    # ------------------ Put your code below ------------------ 
    # so I'm going to find the average of all pixels as if thery were in an array
    # and do the variance the same
    # I'm going to pretend that the images will always be grayscale, so single channel per pixel
    array_like_temp = np.reshape(temp.copy(), -1)

    #use numpy to find mean and variance of the array

    mean_t = np.mean(array_like_temp)
    var_t = np.var(array_like_temp)

                    
    max_corr = 0;
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            mean_s = 0;
            var_s = 0;
            corr = 0;
            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------ 
            array_like_src = np.reshape(src[i:i+temp.shape[0] , j:j+temp.shape[1]], -1)
            
            mean_s = np.mean(array_like_src)
            var_s = np.var(array_like_src)
            
            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------ 
            
            #sum up correlations
            for k in np.arange(i,i+temp.shape[0], 1):
                for l in np.arange(j,j+temp.shape[1], 1):
                    corr += (src[k, l] - mean_s) * (temp[k-i, l-j] - mean_t)

            #divide by variance
            corr = corr / (var_s * var_t)

            #normalize by number of pixels
            corr = corr / (temp.shape[0] * temp.shape[1])

            #print(i, j, corr)
            correlations[str(i)+str(j)] = corr

            if corr > max_corr:
                max_corr = corr;
                location = [i, j];

    #print(max(correlations.keys(),key=(lambda key: correlations[key]) ))
    return location

# load source and template images
source_img = cv2.imread('../img/coins.png',0) # read image in grayscale
temp = cv2.imread('../img/coin.jpg',0) # read image in grayscale

print(source_img.shape)
print(temp.shape)

location = TemplateMatching(source_img, temp, 1);
print(location)
match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)

# Draw a red rectangle on match_img to show the template matching result
# ------------------ Put your code below ------------------ 
cv2.rectangle(match_img, (location[1], location[0]), ( temp.shape[1]+location[1], temp.shape[0]+location[0] ), (0, 0, 255), 5)


# Save the template matching result image (match_img)
# ------------------ Put your code below ------------------ 
cv2.imwrite('match_img.jpg', match_img)


# Display the template image and the matching result
cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
cv2.imshow('TemplateImage', temp)
cv2.imshow('MyTemplateMatching', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()