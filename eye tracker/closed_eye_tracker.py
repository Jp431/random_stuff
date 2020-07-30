import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml') 

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

"""
FORMATTING THE MESSAGES THAT APPEARS IN THE SCREEEN
"""
font = cv2.FONT_HERSHEY_PLAIN
font_size = 2
cap = cv2.VideoCapture(0)

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        cv2.putText(img,'Mostra o rosto ou eu te bato', (10,200), font, font_size+0.45, (0,0,255), font_size, cv2.LINE_AA)
    else:
        for (x,y,w,h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            
            eyes = eye_cascade.detectMultiScale(roi_gray)

            if len(eyes) == 0:
                cv2.putText(img,'Abre o olho, mano', (10,100), font, font_size, (0,0,255), font_size, cv2.LINE_AA)
            else:
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                cv2.putText(img,'Isso, continua trampando ai...', (10,100), font, font_size, (0,255,0), font_size, cv2.LINE_AA)

    # saves the file
    out.write(img)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()