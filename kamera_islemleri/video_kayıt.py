import cv2

cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)#bazı bigisayarlarda hata varebilir cv2.CAP_DSHOW yazılır

fileName="D:\python_\openCV\.idea\output.avi"# kaydolunan yer avi uzantılı olmalı
codec=cv2.VideoWriter_fourcc('W','M','V','2')#videolar ses ve görüntülerden oluşurlar bunları çözmemk için algoritmalar kullanılır, codec bu alogoritmalrı tanıyan yapılardır
#fourcc =medya verilerindeki codecleri 4 karakterli olarak sınıflar, neden olduğu sitesinde var
frameRate=10
resolution=(640,480)#çözünürlük

videoFileOutput=cv2.VideoWriter(fileName,codec,frameRate,resolution)
while 1:
    ret, frame =cap.read()
    videoFileOutput.write(frame)
    frame=cv2.flip(frame, 1)
    cv2.imshow("webcam", frame)
    
    if cv2.waitKey(1)==27:#27 klavyede esc demek
        break


cap.release()
videoFileOutput.release()
cv2.destroyAllWindows()
