import cv2
import math
import mediapipe as mp
import time

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

mpDraw = mp.solutions.drawing_utils
mpPose= mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture("KneeBendVideo.mp4")

st_time =0
en_time = 0
ho_time=0
bended = 0

while True:
    #success variable tells us whether the image is being captured successfully.
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = pose.process(imgRGB)
    #print(result.pose_landmarks)
    #print("------------------------------------")
    if result.pose_landmarks:
        #mpDraw.draw_landmarks(img,result.pose_landmarks,mpPose.POSE_CONNECTIONS)
        points={}
        for id,lm in enumerate(result.pose_landmarks.landmark):
            #height, width, chanel
            h,w,d=img.shape
            #converting coordinates to pixels
            cx,cy=int(lm.x*w),int(lm.y*h)
            #print(id,lm,cx,cy)
            points[id]=(cx,cy)

        #cv2.circle(img,points[23],15,(255,0,0))
        #cv2.circle(img,points[25],15,(255,0,0))
        #cv2.circle(img,points[27],15,(255,0,0))
        
        if (points[27][0]<points[23][0]):
            angle = getAngle(points[23],points[25],points[27])
        
        if angle<140 and angle>0: 
            if st_time==0 :
                st_time = time.time_ns()
            ho_time = (time.time_ns()-st_time)/1000000000
            #threshold = ho_time
            if (ho_time<8.0):
                cv2.putText(img,"Keep your knee bent",(450,50),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
        if angle>140 and angle<250 and st_time != 0:
            en_time = time.time_ns()
            trigger = (en_time-1000000000*ho_time)/1000000000
            diff = (en_time - st_time)/1000000000
            if (trigger>10.0):
                if(diff >= 8.0 ) :
                        bended+= 1
            if angle<30:
                bended=bended
            st_time = 0
            en_time = 0
            ho_time = 0
            
            #if (trigger>0.1):
            #   print("issue") 

    #cv2.line(img, points[23], points[25], (0,0,0), 5)
    #cv2.line(img, points[25], points[27], (0,0,0), 5)

    cv2.putText(img,"Rep Count",(100,60),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)
    cv2.putText(img,str(bended),(100,100),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,0),4)
    cv2.putText(img,"Hold Time",(250,60),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)
    cv2.putText(img,"%.2f"%ho_time,(250,100),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,0),4)
    #cv2.putText(img,"Angle",(600,60),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)
    #cv2.putText(img,"%.2f"%angle,(600,100),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,0),4)

    cv2.imshow("img",img)
    cv2.waitKey(5)