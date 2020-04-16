
import cv2

#create a cascade classifier object
face_cascade=cv2.CascadeClassifier("C:/Users/Prajjwal/Anaconda3/anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

#reading the image as it is
img=cv2.imread('C:/Users/Prajjwal/Desktop/mummy papa 25 marriage anniverasary/photo.jpg')

#reading the image as gray scale image
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#searching the coordinates of the image
faces=face_cascade.detectMultiScale(gray_image,scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in  faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    
    
resized=cv2.resize(img,(int(img.shape[1]/7),int(img.shape[0]/7)))
    
cv2.imshow("Gray",resized)

cv2.waitKey(0)

cv2.destroyAllWindows
