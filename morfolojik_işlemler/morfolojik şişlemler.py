#morfolojik işlemler her zaman binary resimler üzerine yapılır

import cv2
import numpy as np


img=cv2.imread("images (1).png")
kernel= np.ones((5,5),np.uint8)#ones içine yazılan kadar beyaz kğçültür
erosion=cv2.erode(img,kernel,iterations=3)#kernel çekirdek bir tür matris ne kadar yapardsak  resim o kad rbozunuma uğrar
#gürültüleri eleyebilğimiz kadar yüksak olmalı
dilation=cv2.dilate(img,kernel,iterations=3)#beyazlar büyütüyo
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)#gürültülerşeklin dında olursa bununla yok edilir
cloesing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

cv2.imshow("ori",img)
#cv2.imshow("ero",erosion)
#cv2.imshow("dali",dilation)
cv2.imshow("openin",opening)
cv2.imshow("close",cloesing)
cv2.waitKey(0)
cv2.destroyAllWindows()