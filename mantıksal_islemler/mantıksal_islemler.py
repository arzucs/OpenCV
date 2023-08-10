import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=np.zeros((400,400),dtype=np.uint8)
white=(255,255,255)
cv2.rectangle(img1,(50,50),(325,325),white,-1)#400 e 400yük böldüğümüz karede 50ye 50den başla 325e kadar
cv2.imshow("rec",img1)

img2=np.zeros((400,400),dtype=np.uint8)
cv2.circle(img2,(200,200),150,(255,255,255),-1)
cv2.imshow("circ",img2)

bitwiseAnd=cv2.bitwise_and(img1,img2)#1 
bitwiseOr=cv2.bitwise_or(img1,img2)#1 veya 0=1
bitwiseXor=cv2.bitwise_xor(img1,img2)#1ile 1=0 0ile 1=1
bitwiseNot=cv2.bitwise_not(img1)#tersinii alır

titles=["rectangle","circle","bitwiseAnd","bitwiseOr","bitwiseXor","bitwiseNot"]
images=[img1,img2,bitwiseAnd,bitwiseOr,bitwiseXor,bitwiseNot]

for i in range(6):#6tane görüntü
    plt.subplot(2,3,i+1)#iki satır 3sütundan oluşsun, i yi artırsın
    plt.imshow(cv2.cvtColor(images[i],cv2.COLOR_RGB2BGR))
    #imshow rgb olarak görüntürler cvtclor ile renliye a çveirdik,COLOR_RGB2BGR bgr ye çevirdik
    plt.title(titles[i])
    plt.xticks([])#her bir görüntünün matplatlib de bir grafiği aVR ONlrı görmemmize gerek yok ondna içini boş bıarktık
    plt.yticks([])
    
plt.show()


