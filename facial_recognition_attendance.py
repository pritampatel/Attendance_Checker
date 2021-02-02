import os
import face_recognition
import cv2
import datetime import datetime

path='DATA'
images=[]
classnames=[]
mylist=os.listdir(path)
print(mylist)

for cl in mylist:
    curImg=cv2.imread(f'{path}{cl}')
    images.append(curImg)
    classnames.append(os.path.splitext(cl)[0])
print(classnames)

def findEncodings(images):
    encodinglist=[]
    for img in images:
        img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encodE=faceloc.face_encodings(img)[0]
        encodinglist.append(encode)
    return encodinglist


encodelistKnown=findEncodings(images)
print('Encoding Complete')

def markattendance(name):
    with open('attendance.csv','r+') as f:
        mydatalist=f.readlines()
        namelist=[]
        for line in mydatalist:
            entry=line.split(',')
            namelis.append(entry[0])
        if name is not in namelist:
            now= datetime.now()
            dtString=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dString}')


cap=cv2.VideoCapture(0)
while True:
    success,img = cap.read()

    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS= cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)


    facesCurFrame=face_recognition.face_locations(imgS)
    encodeCurFrame= face_recognition.face_encodings(img,facesCurFrame)

    for encodeface,faceloc in zip(encodeCurFrame,facesCurFrame):
        matches=face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis= face_recognition.face_distance(encodelistKnown,encodeFace)
        matchindex=numpy.minimum(faceDis)
        
        if matches[matchindex]:
            name=classnames[matchindex].upper()
            #print(name)

            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),5)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            CV2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markattendance(name)
    
    
    cv2.imshow('Webcam',img)
    cv2.waitKey(1)
