import cv2
import numpy as np
from matplotlib import pyplot as plt#burda toplu tek ekranda görmek için gereken kütüphane

#img=cv2.imread("foto.jpg")
img=cv2.imread("qrkod.jpeg")


replicate=cv2.copyMakeBorder(img,200,200,100,100,cv2.BORDER_REPLICATE)
reflect=cv2.copyMakeBorder(img,200,200,100,100,cv2.BORDER_REFLECT)
reflect101=cv2.copyMakeBorder(img,200,200,100,100,cv2.BORDER_REFLECT101)
wrap=cv2.copyMakeBorder(img,200,200,100,100,cv2.BORDER_WRAP)
constant=cv2.copyMakeBorder(img,200,200,100,100,cv2.BORDER_CONSTANT,value=(255,0,180))

####
laplacian=cv2.Laplacian(img,cv2.CV_64F)
sobel=cv2.Sobel(img,cv2.CV_64F, 0 ,1, ksize=5)
sobely=cv2.Sobel(img, cv2.CV_64F, 1, 0,ksize=5)
canny=cv2.Canny(img,50,200)


cv2.imshow("laplacian", laplacian)
cv2.imshow("sobel",sobel)
cv2.imshow("sobely",sobely)



#tek tek pencerelerde görüntüleme için
"""
cv2.imshow("orjinal", img)
cv2.imshow("replicate",replicate)
cv2.imshow("reflect101",reflect101)
cv2.imshow("reflect",reflect)
cv2.imshow ("wrap",wrap)
cv2.imshow("constant",constant)
"""


#toplu tek ekranda görmek için
"""
plt.subplot(231),plt.imshow(img,'gray'),plt.title("orjinal")
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title("replicate")
plt.subplot(233),plt.imshow(reflect101,'gray'),plt.title("reflect101")
plt.subplot(234),plt.imshow(reflect,'gray'),plt.title("reflect")
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title("wrap")
plt.subplot(236),plt.imshow(constant,'gray'),plt.title("constant")

plt.show()
"""
plt.subplot(231),plt.imshow(img,'gray'),plt.title("orjinal")
plt.subplot(232),plt.imshow(laplacian,'gray'),plt.title("laplacian")
plt.subplot(233),plt.imshow(sobel,'gray'),plt.title("sobel")
plt.subplot(234),plt.imshow(sobely,'gray'),plt.title("sobely")
plt.subplot(235),plt.imshow(canny,'gray'),plt.title("canny")

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()