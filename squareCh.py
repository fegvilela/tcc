import cv2

image = cv2.imread("156.jpeg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilated = cv2.dilate(thresh,kernel,iterations = 0)
_,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

i=5
for contour in contours:

    [x,y,w,h] = cv2.boundingRect(contour)

    cv2.imwrite(str(i)+".jpg",image[y:y+h,x:x+w])
    i=i+1
