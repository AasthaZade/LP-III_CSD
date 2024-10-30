import cv2

# Load the image in grayscale
img = cv2.imread('flower.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if img is None:
    print("Error: Could not load the image.")
else:
    # Apply simple thresholding
    threshold_value = 127  # You can change this value
    max_value = 255  # Max intensity to assign for pixels above the threshold

    # Apply the thresholding function
    _, thresh_img = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_BINARY)
    

    # Display the original and thresholded images
    cv2.imshow("Original Grayscale Image", img)
    cv2.imshow("Thresholded Image", thresh_img)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("threshold.jpg",thresh_img)

'''
you can replace cv2.THRESH_BINARY with other thresholding methods:

cv2.THRESH_BINARY_INV: Inverse binary thresholding.
cv2.THRESH_TRUNC: Pixels above the threshold are set to the threshold value.
cv2.THRESH_TOZERO: Pixels below the threshold are set to 0.
cv2.THRESH_TOZERO_INV: Inverse of the TOZERO method.
'''