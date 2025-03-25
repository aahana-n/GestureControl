import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
import subprocess
#################################################
wCam, hCam = 720, 560
#################################################
def set_volume(volume):
    " " "Adjust sysytem volume(0-100)" " "
    volume = max(0, min(100, int(volume)))
    subprocess.run(["osascript", "-e", f"set volume output volume {volume}"])

output = subprocess.run(["osascript", "-e", "output volume of (get volume settings)"], capture_output=True, text=True)
current_volume = int(output.stdout.strip())
print("Current Volume:", current_volume)

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
cap.set(cv2.CAP_PROP_FPS, 80)
cap.set(cv2.CAP_PROP_BUFFERSIZE,1)
pTime = 0


detector = htm.handDetector(detectionCon = 0.7)

min_length = 40
max_length = 200
min_vol = 0
max_vol = 100


while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    volume = current_volume
    if len(lmList) != 0 :
        #print(lmList[4], lmList[8])


        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1, y1), 15, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255,0,255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255,0,255), 3)
        cv2.circle(img, (cx, cy), 15, (255,0,255), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)
        #print(length)

        volume = np.interp(length, [20,200], [0,100])
        subprocess.run(["osascript", "-e", f"set volume output volume {int(volume)}"])
        cv2.putText(img, f'Vol: {int(volume)}', (50,150), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 3)

        if length < 40:
            cv2.circle(img, (cx, cy), 15, (0,255,0), cv2.FILLED)

        

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,f'FPS: {int(fps)}',(40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 3)

    cv2.imshow("Img",img)
    cv2.waitKey(1)