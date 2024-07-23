import cv2
import mediapipe as mp
import mouse_action

mp_drawing= mp.solutions.drawing_utils
#mp_holistic=mp.solutions.holistic
mp_hands= mp.solutions.hands

#holistic= mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5)
hands=mp_hands.Hands(min_detection_confidence=0.7,min_tracking_confidence=0.7)
cap= cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break

    # Remove the mirror effect
    frame = cv2.flip(frame, 1) 

    # Convert the BGR image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    
    # Process the image and detect the hand landmarks
    results = hands.process(image)

    # Convert the image color back so it can be displayed
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # Draw hand landmarks
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the coordinates of the index finger tip (landmark 8)
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Convert the normalized coordinates to pixel values
            height, width, _ = image.shape
            x = int(index_finger_tip.x * width)
            y = int(index_finger_tip.y * height)

            # Move the mouse
            mouse_action.move_mouse(x, y, width, height)



    cv2.imshow('Raw Webcam Feed', image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
        
cap.release()
cv2.destroyAllWindows()

