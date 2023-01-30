import cv2
import mediapipe as mp

mpDraw = mp.solutions.drawing_utils
mpPose= mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture("KneeBendVideo.mp4")

while True:
    #success variable tells us whether the image is being captured successfully.
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = pose.process(imgRGB)
    print(result.pose_landmarks)
    print("------------------------------------")
    if result.pose_landmarks:
        mpDraw.draw_landmarks(img,result.pose_landmarks,mpPose.POSE_CONNECTIONS)


cv2.imshow("img",imgRGB)
cv2.waitKey(5)