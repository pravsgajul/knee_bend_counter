import cv2
import math
import mediapipe as mp
import timeit

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

mpDraw = mp.solutions.drawing_utils
mpPose= mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture("KneeBendVideo.mp4")
bent = False
counter=0
start=0

while True:
    #success variable tells us whether the image is being captured successfully.
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = pose.process(imgRGB)
    #print(result.pose_landmarks)
    #print("------------------------------------")
    if result.pose_landmarks:
        mpDraw.draw_landmarks(img,result.pose_landmarks,mpPose.POSE_CONNECTIONS)
        points={}
        for id,lm in enumerate(result.pose_landmarks.landmark):
            #height, width, chanel
            h,w,d=img.shape
            #converting coordinates to pixels
            cx,cy=int(lm.x*w),int(lm.y*h)
            #print(id,lm,cx,cy)
            points[id]=(cx,cy)

        cv2.circle(img,points[23],15,(255,0,0))
        cv2.circle(img,points[25],15,(255,0,0))
        cv2.circle(img,points[27],15,(255,0,0))
        
        angle = getAngle(points[23],points[25],points[27])
        
        start = timeit.default_timer()
        if not bent and angle<140:
            print("Bent")
            bent=True
            counter+=1
        if angle>140:
            bent=False

    cv2.line(img, points[23], points[25], (0,0,0), 5)
    cv2.line(img, points[25], points[27], (0,0,0), 5)
    cv2.putText(img,str(counter),(100,150),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(55,55,55),8)
    cv2.putText(img,str(start),(300,150),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(55,55,55),8)
    cv2.putText(img,str(reptimer),(400,150),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(55,55,55),8)

    cv2.imshow("img",img)
    cv2.waitKey(5)