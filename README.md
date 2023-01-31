# knee bend counter
 
<h2>INSTRUCTIONS OR METHOD USED TO BUILD KNEE BEND TRACKER</h2>
IDE used: Virtual Studio Code<br>
Libraries Used: cv2, Mediapipe, math, time<br>
1.	Initially we created objects mpDraw, mpPose and Pose. These are objects created using mediapipe.<br>
2.	To read the video, we used the function called VideoCapture in cv2. We define a few variables and initialize them to 0.<br>
3.	We use pose_landmarks from the mediapipe library to map to the body of the person. Pose landmarks gives x-coordinate, y-coordinate, depth and visibility.<br>
4.	For id and landmarks enumerated after pose_landmarks, we convert the co-ordinates of the ids into pixels and store them in a library called points.<br>
5.	We then put a constraint that the x-coordinate of the ankle should always be less than the x-coordinate of the hip.<br>
6.	Then we calculate the angle between the ankle, knee and the hip. A function has been defined for the same.<br>
7.	If the angle is less than 140, we start the holding timer and record the start time. If holding time is less than 8 seconds, we display the message “keep your knee bent”.<br>
8.	If the angle is greater than 140, then we calculate the duration of the time that the leg was in the bent position. If it was less than eight the counter is not incremented. If the duration was greater than 8 secs, the counter is incremented and all the times are reset to 0.<br>
9.	We then just display everything in the output window using cv2.imshow.<br>

