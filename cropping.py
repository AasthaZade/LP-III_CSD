
import cv2

# Load the image
img = cv2.imread('flower.jpg')

# Check if the image was successfully loaded
if img is None:
    print("Error: Could not load the image.")
else:
    # Print the shape of the image (height, width, channels)
    print(img.shape)

    # Display the original image
    cv2.imshow("Original", img)

    # Define the cropping coordinates
    cropped_img = img[100:280, 150:300]

    # Display the cropped image
    cv2.imshow("Cropped", cropped_img)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("cropped.jpg",cropped_img)


