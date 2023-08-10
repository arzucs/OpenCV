import cv2
import numpy as np
import matplotlib.pyplot as plt #histogram çizdirmek için gerekli


img=cv2.imread("D:/python_/openCV/.idea/histogram/ana_resim.png")# resmin ismi ya da olduğu yerin uzantısı 
b,g,r =cv2.split(img) # cv2.split(img) bgr yi birbirinden ayırıp değişkenlere atar

cv2.imshow("manzaram",img)
"""
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
"""

plt.hist(img.ravel(),256,[0,256])
#tüm verilweri tek yatay sıraya dizdi, renk değeri
plt.hist(b.ravel(), 256,[0, 256])
plt.hist(g.ravel(), 256,[0, 256])
plt.hist(r.ravel(), 256,[0, 256])

plt.show()
cv2.destroyAllWindows()




