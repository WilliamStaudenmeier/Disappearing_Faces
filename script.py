import cv2
import time
import numpy as np



hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

# open webcam
cap = cv2.VideoCapture('test_video.mp4')

time.sleep(3)
n_frame = 0


while True:
    _, frame = cap.read()
    frame = cv2.rotate(frame,rotateCode = 1) 
    n_frame += 1

    if n_frame == 20:
        frame = cv2.resize(frame, (640, 480))
        frame = cv2.rotate(frame,rotateCode = 1) 
        first_frame = frame.copy()
        first_frame = cv2.rotate(first_frame, rotateCode = 1) 
        break



_, frame = cap.read()
frame = cv2.rotate(frame,rotateCode = 1) 
frame = cv2.resize(frame, (640, 480))

while True:
 

    _, frame = cap.read()


    frame = cv2.resize(frame, (640, 480))
    frame = cv2.rotate(frame,rotateCode = 1) 


    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

   
    boxes, weights = hog.detectMultiScale(gray,
                                          winStride=(8, 8),
                                          padding=(16, 16),
                                          scale=1.05)


    original = frame.copy()
    rectangle = frame.copy()
    
    for (x, y, w, h) in boxes:

        crop_img = first_frame[y:y + h, x:x + w]
        frame[y:y + h, x:x + w] = crop_img
        
     
        cv2.rectangle(rectangle, (x, y), (x+w, y+h), (0, 255, 0), 2)

 
    cv2.imshow('Current Frame', frame)
  
    cv2.imshow('Train Frame', rectangle)

    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
