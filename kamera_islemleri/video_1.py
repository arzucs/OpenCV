#kameraya erişim
import cv2

cap=cv2.VideoCapture(0)#0ise pc kamerası 1ile başka bağlı olan bir kamera

while 1:
    ret ,frame=cap.read()#frame ler tek tek okundu ve hafızada
    
    frame=cv2.flip(frame,1) #normalde aldığımmız görüntü aynadakiyle aynı ama y eksenine göre simetri alırsak düzeltilmiş olur
    #frame lerin y eksenine göre simetrisi demek
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    
    cv2.imshow("webcam",frame)#frame leri izle
    cv2.imshow("gray",gray)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):#1 milisaniye,klavyeden q alınca döngüyü kır
        break

cap.release()#video ile işim bitti demek, bu yapılmazsa video hala işlemde gibi görünür ve başka işlem yapılamaz
cv2.destroyAllWindows()