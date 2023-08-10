import cv2
import numpy as np

img_rgb=cv2.imread("ana_resim.jpg")
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)

nesne=cv2.imread("nesne_2.jpg", 0)

w,h=nesne.shape[::-1]#4 paremetre var ilk 2 paremetre alınmadı sonraki 2yi al demiş olduk
#cv2.matchTemplate: basit nesne bulma işlemlerinde kullanılabilir resim çok küçük de değiştirilse nesne bulunamaz
res=cv2.matchTemplate(img_gray, nesne, cv2.TM_CCOEFF_NORMED)
threshold=0.8 #doğruluk payı

loc=np.where(res>threshold) #eşleştirmenin %80den büyük olduğu kısımlarda loc a kaydet

for n in zip (*loc[::-1]):
    cv2.rectangle(img_rgb,n,(n[0]+w, n[1]+h),(0,0,255),2 )
#                             n noktasının 0. parametresi:sol üst x noktasıdır,sol üst köşenin y bileşeni

cv2.imshow("bulunan nesneler", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()