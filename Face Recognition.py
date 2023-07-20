import os
import cv2 as cv
import numpy as np
import face_recognition 

path = 'Face Detection\Faces' 
images = []
className = []
myList = os.listdir(path)
# print(myList)



for cls in myList:
    currentImg = cv.imread(f'{path}\{cls}')
    images.append(currentImg)
    className.append(os.path.splitext(cls)[0])
    # print(cls)
    




def encodeImg(images):
    encodedList = []
    for img in images:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodedList.append(encode)
    return encodedList

encodeListKnown = encodeImg(images)
print("Recognition done !!!")


capture = cv.VideoCapture(0)

while True:
    sucess, img  =capture.read()
    resizedImg = cv.resize(img, (0,0), None, 0.25, 0.25)
    resizedImg = cv.cvtColor(resizedImg, cv.COLOR_BGR2RGB)

    facesCurrFrame = face_recognition.face_locations(resizedImg)
    encodedCurrFrame = face_recognition.face_encodings(resizedImg, facesCurrFrame)

    for encodeFace, faceLoc in zip(encodedCurrFrame, facesCurrFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = className[matchIndex].upper()
            # print(name)
            y1,x1,y2,x2 = faceLoc
            y1,x1,y2,x2 = y1*4,x1*4,y2*4,x2*4
            cv.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
            cv.putText(img,name, (x1+6,y2-6), cv.FONT_HERSHEY_COMPLEX,1, (0,255,255), 2)


    cv.imshow("webcam", img)
    cv.waitKey(1)












