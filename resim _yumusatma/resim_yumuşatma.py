import cv2
import numpy as np


#blur
#
img=cv2.imread("foto.jpg")
averanging=cv2.blur(img,(3,7))#3,3kernel değeri
#
#GAUSSİAN

img=cv2.imread("foto.jpg")
gaussian=cv2.GaussianBlur(img,(3,7),0)#sıfır standart sapma ,
#kernel boyutuna bağlı standart sapmayı kendi hesaplamış olur sıfır olduğunda

#MEDİAN BLUR
img=cv2.imread("foto2.jpg")
median=cv2.medianBlur(img,11)


cv2.imshow("origin",img)
cv2.imshow("gausian",gaussian)
cv2.imshow("blur",averanging)
cv2.imshow("median",median)


cv2.waitKey(0)
cv2.destroyAllWindows()
