import cv2
import numpy as np

def nothing(x):
    pass


canvas=np.zeros((512,512,3),dtype=np.uint8)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)


cv2.createTrackbar("R","image",0,255,nothing)
#red=R ,nerde olduğu, 0ile 255 ardası renkler,
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)
cv2.createTrackbar("Switch","image",0,1,nothing)

while True: #kızaktaki değerleri hep görmemiz gerek
    cv2.imshow("image",canvas)
    if cv2.waitKey(1) & 0xFF==ord('q'):#eger q ya basarken döngüyü kır pencereyi kapat
        break
    s=cv2.getTrackbarPos("Switch","image")
    r=cv2.getTrackbarPos("R","image")#trackbar posiyonlarını çekmek için
    g=cv2.getTrackbarPos("G","image")
    b=cv2.getTrackbarPos("B","image")
    
    if s==1:#eğer switch 1 ise yap
    #çekilen değerlerin tuvalde gözükmesini sağlamak için
        canvas[:]=[b,g,r]#tüm b g r değerlerini tara; daha önceden çektiğimiz değerklere eşitle
    else:
        canvas[:]=[0,0,0]

cv2.destroyAllWindows()