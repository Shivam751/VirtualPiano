import cv2
import mediapipe as mp
import time
import pyautogui
import pydirectinput as pyi

def Press(key):
    print("pressed")
    pyautogui.press(key)
    
cap=cv2.VideoCapture(0)
cv2.namedWindow('img',cv2.WINDOW_NORMAL)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
pTime = 0
cTime = 0

while True:
    _,img=cap.read()
    img = cv2.resize(img,(580,600))
    H,W,C = img.shape
    img = cv2.flip(img,1)
    
    cv2.rectangle(img, (5,0), (40,250), (255,255,255),1)
    cv2.rectangle(img, (43,0), (75,250), (255,255,255),1)
    cv2.rectangle(img, (78,0), (105,250), (255,255,255),1)
    cv2.rectangle(img, (108,0), (140,250), (255,255,255),1)
    cv2.rectangle(img, (143,0), (175,250), (255,255,255),1)
    cv2.rectangle(img, (178,0), (205,250), (255,255,255),1)
    cv2.rectangle(img, (208,0), (240,250), (255,255,255),1)
    cv2.rectangle(img, (243,0), (275,250), (255,255,255),1)
    cv2.rectangle(img, (278,0), (305,250), (255,255,255),1)
    cv2.rectangle(img, (308,0), (340,250), (255,255,255),1)
    cv2.rectangle(img, (343,0), (375,250), (255,255,255),1)
    cv2.rectangle(img, (378,0), (405,250), (255,255,255),1)
    cv2.rectangle(img, (408,0), (440,250), (255,255,255),1)
    cv2.rectangle(img, (443,0), (475,250), (255,255,255),1)
    cv2.rectangle(img, (478,0), (505,250), (255,255,255),1)
    cv2.rectangle(img, (508,0), (540,250), (255,255,255),1)
    cv2.rectangle(img, (543,0), (575,250), (255,255,255),1)

    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)         
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                h,w,c=img.shape
                p,q=int(lm.x*w),int(lm.y*h)
                # p=cx,q=cy
                if(id==4 or id==8 or id==12 or id==16 or id==20):
                    if p > 5 and q > 0 and p < 40 and q < 250:
                        print('Q')
                        Press('Q') 
                        break      
                    if p > 43 and q > 0  and p < 75 and q < 250:
                        Press('W') 
                        break      
                    if p > 78 and q > 0 and p < 105 and q < 250:
                        Press('E') 
                        break      
                    if p > 108 and q > 0 and p < 140 and q < 250:
                        Press('R') 
                        break      
                    if p > 143 and q > 0 and p < 175 and q < 250:
                        Press('T') 
                        break      
                    if p > 178 and q > 0 and p < 205 and q < 250:
                        Press('Y') 
                        break      
                    if p > 208 and q > 0 and p < 240 and q < 250:
                        Press('U')  
                        break      
                    if p > 243 and q > 0 and p < 275 and q < 250:
                        Press('I')
                        break      
                    if p > 278 and q > 0 and p < 305 and q < 250:
                        Press('O') 
                        break      
                    if p > 308 and q > 0 and p < 340 and q < 250:
                        Press('P') 
                        break      
                    if p > 343 and q > 0 and p < 375 and q < 250:
                        Press('Z') 
                        break      
                    if p > 378 and q > 0 and p < 405 and q < 250:
                        Press('X')
                        break 
                    if p > 408 and q > 0 and p < 440 and q < 250:
                        Press('C')
                        break 
                    if p > 443 and q > 0 and p < 475 and q < 250:
                        Press('V')
                        break 
                    if p > 478 and q > 0 and p < 505 and q < 250:
                        Press('B')
                        break 
                    if p > 508 and q > 0 and p < 540 and q < 250:
                        Press('N')
                        break
                    if p > 543 and q > 0 and p < 575 and q < 250:
                        Press('M')
                        break      
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
    
    cv2.imshow('img',img) 
    
    key = cv2.waitKey(1)
    if(key==27):
        break

cap.release()
cv2.destroyAllWindows()