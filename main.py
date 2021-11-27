import mediapipe as mp
import cv2 as cv
import time
import sound


my=cv.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils



while True:

    sucess,img=my.read()
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
          for id,lm in enumerate(handlms.landmark):
              h,w,c=img.shape
              cx,cy=int(lm.x*w),int(lm.y*h)
              if id==8 and (cx>430 and cx>350):
               x=sound.Play.start(True)
               print(1)
              if id==4 and (cx>430 and cx>350):
               x=sound.Play.ok(True)
               print(2)


          mpDraw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)




    cv.imshow("image",img)


    if cv.waitKey(1) & 0xFF ==ord("q"):
        break
