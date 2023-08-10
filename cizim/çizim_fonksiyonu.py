import cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8) +255 #(0,0,0)+255=(255,255,255) =beyaz
#zeros içini sıfırkar ile doldurur pencere siyah gelir
#512 ye 512 büyklükte
#dtype=veri tipi
cv2.line(canvas, (0,0), (512,512), (250,0,0), 5)#çizgi
#başlangıç noktası(sol üst köşe), nereye kadar(sağ alt köşe), renk(mavi), kalınlık
cv2.rectangle(canvas,(250,300),(400,400),(0,250,0),-1)#-1 olursa içi dolu olur
#ilk nereye yapılacak, 150ye 150den başla,320ye 320de bitsin.renk(yeşil), kalınlık
cv2.circle(canvas,(100,200),100,(0,0,255),-1)
#merkez konumi,yarıçap,renk, kalınlık

font=cv2.FONT_HERSHEY_SIMPLEX
font1=cv2.FONT_HERSHEY_TRIPLEX
font2=cv2.FONT_HERSHEY_PLAIN
cv2.putText(canvas,"opencv",(10,100),font,4,(244,158,66),4,cv2.LINE_AA)
#     nereye,ne yazılcak,konumu(sol alt köşe),font büyüklüğü,renk,kalınlık,yazı tipi
cv2.putText(canvas,"hadi",(10,200),font1,4,(0,158,100),4,cv2.LINE_AA)
cv2.putText(canvas,"NABEER",(10,300),font2,4,(0,200,100),4,cv2.LINE_AA)



cv2.imshow("canvas",canvas)
cv2.waitKey()
cv2.destroyAllWindows()