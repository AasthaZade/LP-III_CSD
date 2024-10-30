import cv2
img_grayscale = cv2.imread('test.png',0)
img_color = cv2.imread('test.png',1)
img_unchanged = cv2.imread('test.png',-1)
 
# The function cv2.imshow() is used to display an image in a window.
cv2.imshow('graycsale image',img_grayscale)
cv2.imshow('color',img_color)
cv2.imshow('unchanged',img_unchanged)
# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv2.waitKey(0)
 
# cv2.destroyAllWindows() simply destroys all the windows we created.
cv2.destroyAllWindows()
 
# The function cv2.imwrite() is used to write an image.
cv2.imwrite('grayscale.jpg',img_grayscale)
cv2.imwrite('color.jpg',img_color)
cv2.imwrite('unchanged.jpg',img_unchanged)
