# bir pencereden 4 görüntü alma
import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret, frame= cap.read()
    frame=cv2.flip(frame,1)#y eksenine göre simetri alma
    
    width=int(cap.get(3))
    height=int(cap.get(4))
    
    image=np.zeros(frame.shape, np.uint8)

    smaller_frame=cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    
    image[:height//2, :width//2]=cv2.rotate(smaller_frame,cv2.ROTATE_180) #top left
    image[height//2:, :width//2]=smaller_frame#bottom left
    image[:height//2, width//2:]=cv2.rotate(smaller_frame, cv2.ROTATE_180) #top right
    image[height//2:, width//2:]=smaller_frame #bottom right

    cv2.imshow("frame",image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    