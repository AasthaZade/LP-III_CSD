import cv2

# Read an image
img = cv2.imread('a.jpeg')
	
#Make copy of the image
imageLine = img.copy()
# Draw the image from point A to B
pointA = (200,80)
pointB = (450,80)
cv2.line(imageLine, pointA, pointB, (255, 255, 0), thickness=3)
# Display the image
cv2.imshow('Image', img)
#display line
cv2.imshow('Image Line', imageLine)
# Make a copy of image
imageCircle = img.copy()
# define the center of circle
circle_center = (174,103)
# define the radius of the circle
radius =100
#  Draw a circle using the circle() Function
cv2.circle(imageCircle, circle_center, radius, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA) 
# Display the result
cv2.imshow("Image Circle",imageCircle)
# make a copy of the original image
imageRectangle = img.copy()
# define the starting and end points of the rectangle
start_point =(73,85)
end_point =(170,118)
# draw the rectangle
cv2.rectangle(imageRectangle, start_point, end_point, (0, 0, 255), thickness= 3, lineType=cv2.LINE_8) 
# display the output
cv2.imshow('imageRectangle', imageRectangle)
# make a copy of the original image
imageEllipse = img.copy()
# define the center point of ellipse
ellipse_center = (134,47)
# define the major and minor axes of the ellipse
axis1 = (127,25)
axis2 = (132,103)
# draw the ellipse
#Horizontal
cv2.ellipse(imageEllipse, ellipse_center, axis1, 0, 0, 360, (255, 0, 0), thickness=3)
#Vertical
cv2.ellipse(imageEllipse, ellipse_center, axis2, 90, 0, 360, (0, 0, 255), thickness=3)
# display the output
cv2.imshow('ellipse Image',imageEllipse)
cv2.waitKey(0)
cv2.destroyAllwindows()
cv2.imwrite('lineimg.jpeg',imageLine)
cv2.imwrite('eclipseimg.jpeg',imageEllipse)
cv2.imwrite('circleimg.jpeg',imageCircle)
cv2.imwrite('rectimg.jpeg',imageRectangle)