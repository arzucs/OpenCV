import cv2

img=cv2.imread("foto.jpg")
rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("BGR",img)
cv2.imshow("RGB",rgb_img)
cv2.imshow("HSV",hsv_img)
cv2.imshow("GRAY",gray_img)

cv2.waitKey()
cv2.destroyAllWindows()