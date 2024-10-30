import cv2
import numpy as np

# Load the image
img = cv2.imread('flower.jpg')

# Create a mask initialized to 'probably background' everywhere
mask = np.zeros(img.shape[:2], np.uint8)

# Create two arrays that will be used by Grabcut to model foreground and background
bgdModel = np.zeros((1, 65), np.float64)  # Background model
fgdModel = np.zeros((1, 65), np.float64)  # Foreground model

# Define the bounding box for the object
rect = (50, 50, 450, 290)  # You can adjust this to your object location

# Apply Grabcut with the initial bounding box
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Modify the mask so that 0 and 2 are background and 1 and 3 are foreground
# cv2.GC_BGD, cv2.GC_PR_BGD are labeled as 0, 2; and cv2.GC_FGD, cv2.GC_PR_FGD are labeled as 1, 3 respectively
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Apply the mask to the original image
segmented_img = img * mask2[:, :, np.newaxis]

# Display the segmented image
cv2.imshow('Segmented Image', segmented_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the result
cv2.imwrite('segmented_flower.jpg', segmented_img)
