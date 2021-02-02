import cv2
import numpy as np
import matplotlib.pyplot as plt
import face_recognition
#path='/DATA/'
img1=face_recognition.load_image_file('/DATA/musk1.jpg')
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2= face_recognition.load_image_file('DATA/musk2.jpg')
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

faceloc=face_recognition.face_locations(img1)[0]
encoding=faceloc.face_encodings(faceloc)[0]
cv2.rectangle(img1,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,0),5)

faceloc2=face_recognition.face_locations(img2)[0]
encoding2=facelo2c.face_encodings(faceloc)[0]
cv2.rectangle(img2,(faceloc2[3],faceloc2[0]),(faceloc2[1],faceloc2[2]),(0,255,0),5)

results=face_recognition.compare_faces([encoding],encoding2)
face_dis=face_recognition.face_distance([encoding],encoding2)
cv2.putText(img2,f"{results} {round(face_dis[0],2)}",(50,50),cv2.FONT_HERSHEY_COMPLEX,(200,200,200),10)
print(face_dis)