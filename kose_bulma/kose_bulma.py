import cv2
import numpy as np
from matplotlib import pyplot as plt 

img=cv2.imread("corner2.jpg") # resmin ismi ya da olduğu yerin uzantısı 

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)


koseler=cv2.goodFeaturesToTrack(gray,100,0.01,10)#cv2.goodFeaturesToTrack() kullanarak ilk 100 köşeyi bulur
koseler=np.int0(koseler)

for kose in koseler: #Köşeleri yineleyin ve o konumda bir daire çizin
    x,y=kose.ravel()
    cv2.circle(img,(x ,y),3,255,-1)

cv2.imshow("koseler1",img)     
cv2.waitKey(0)
cv2.destroyAllWindows()