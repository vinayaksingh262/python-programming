import numpy as np
import cv2
import mediapipe as mp
from collections import deque

# Initialize Mediapipe Hand Tracking
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Variables for Drawing
bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]
blue_index, green_index, red_index, yellow_index = 0, 0, 0, 0

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
colorIndex = 0

# Canvas Setup
paintWindow = np.ones((471, 636, 3), dtype=np.uint8) * 255
cv2.rectangle(paintWindow, (40, 1), (140, 65), (0, 0, 0), 2)
cv2.rectangle(paintWindow, (160, 1), (255, 65), colors[0], -1)
cv2.rectangle(paintWindow, (275, 1), (370, 65), colors[1], -1)
cv2.rectangle(paintWindow, (390, 1), (485, 65), colors[2], -1)
cv2.rectangle(paintWindow, (505, 1), (600, 65), colors[3], -1)
cv2.putText(paintWindow, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
cv2.putText(
    paintWindow, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2
)
cv2.putText(
    paintWindow, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2
)
cv2.putText(
    paintWindow, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2
)
cv2.putText(
    paintWindow, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 2
)

# Webcam Setup
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame with MediaPipe
    result = hands.process(rgb_frame)
    index_finger = None

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get fingertip position (landmark 8 - index finger tip)
            x = int(hand_landmarks.landmark[8].x * w)
            y = int(hand_landmarks.landmark[8].y * h)
            index_finger = (x, y)

            # Check if the user selects a button
            if colorIndex == 0:
                if blue_index >= len(bpoints):
                    bpoints.append(deque(maxlen=512))
                bpoints[blue_index].appendleft(index_finger)
            elif colorIndex == 1:
                if green_index >= len(gpoints):
                    gpoints.append(deque(maxlen=512))
                gpoints[green_index].appendleft(index_finger)
            elif colorIndex == 2:
                if red_index >= len(rpoints):
                    rpoints.append(deque(maxlen=512))
                rpoints[red_index].appendleft(index_finger)
            elif colorIndex == 3:
                if yellow_index >= len(ypoints):
                    ypoints.append(deque(maxlen=512))
                ypoints[yellow_index].appendleft(index_finger)

    # Draw lines
    points = [bpoints, gpoints, rpoints, ypoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                cv2.line(
                    paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2
                )

    cv2.imshow("Virtual Painter", frame)
    cv2.imshow("Paint", paintWindow)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
