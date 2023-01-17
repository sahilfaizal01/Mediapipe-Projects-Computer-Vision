import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)
pd = PoseDetector()

while(True):
    ret, img = cap.read()
    pd.findPose(img,draw=0)
    lmlist, bbox = pd.findPosition(img,draw=0)
    #print(lmlist)
    if len(lmlist) != 0:
        right_eye = lmlist[5]
        rx, ry = right_eye[1:-1]
        cv2.circle(img,(rx,ry),5,(0,0,255),4)
        
        left_eye = lmlist[2]
        lx, ly = left_eye[1:-1]
        cv2.circle(img,(lx,ly),5,(0,255,0),4)
    
    cv2.imshow('frame',img)
    key = cv2.waitKey(1)
    if key== ord('q'):
        break

cv2.destroyAllWindows()