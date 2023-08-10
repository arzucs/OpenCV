import cv2
img=cv2.imread("ana_resim")#cv2.IMREAD_GRAYSCALE ve 0 resmin siyah beyaz olamsı
#print(img) #sadece bunu yazarsak resmin parametrelerini yazdırır
img=cv2.resize(img,(100,200))#orjinal resmi boyutlandırdır
cv2.namedWindow("image",cv2.WINDOW_NORMAL)#normal sayesinde pencere boyutunu istediğimiz gibi ayarlarız


cv2.imshow("image",img)#açılan pencere adı image oldu
#cv2.imwrite("copy_2.jpg",img)#img isimli resmi copy olarak kaydede-
cv2.waitKey()#bu resmin acılıp kapanamsını ayarlamak için içine ne yazarsak mili saniye cind-sinden açılıp kapanır
#0 yazarsak açık kalır bir tuşa bazsınca kapanır, boş da kalabilir
cv2.destroyAllWindows()#açık olan tüm pencereleri kapat
