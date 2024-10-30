import cv2
image= cv2.imread('flower.jpg')
cv2.imshow('flower org',image)

dw=300 #down width
dh=200 #down height
down_points=(dw,dh)
resize = cv2.resize(image,down_points,interpolation=cv2.INTER_LINEAR)
cv2.imshow("resized image",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("resized.jpg",resize)
