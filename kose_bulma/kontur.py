import cv2

img=cv2.imread("kontur.jpg") # resmin ismi ya da olduğu yerin uzantısı 

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#gri formatta işlem yapmak dah kolay olur
edged=cv2.Canny(gray,50,200)#canny şekillerin köşelerini bulmak için kullanılan fonksiyon

cv2.imshow("canny",edged)

counters ,hierarchy= cv2.findContours(edged, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#                                           ,kontur modu hijerarşi ile ilgili bazı bilgiler bulunur,kontur yaklaşım metodunu temsil eder

print("numbers of counters: ", len(counters))#kontur sayısı

cv2.drawContours(img,counters,-1,(255,0,200),4)#counters[2]
#                   konturları tutan değişken, tüm kanturlar her şeklin konturu,rengi,kalınlığı

cv2.imshow("Counters",img)

cv2.waitKey(0)
cv2.destroyAllWindows()