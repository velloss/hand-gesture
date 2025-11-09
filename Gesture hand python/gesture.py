import cv2
import mediapipe as mp 

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

#untuk menganali gesture
def recognize_gesture(hand_landmarks):
    #ambil posisi ujung jari
    ujung_jempol = hand_landmarks.landmarks[mp_hands.Handlandmark.THUMB_TIP]
    ujung_telunjuk = hand_landmarks.landmarks[mp_hands.Handlandmark.INDEX_FINGER_TIP]
    ujung_tengah = hand_landmarks.landmarks[mp_hands.Handlandmark.MIDDLE_FINGER_TIP]
    ujung_manis = hand_landmarks.landmarks[mp_hands.Handlandmark.RING_FINGER_TIP]
    ujung_kelingking = hand_landmarks.landmarks[mp_hands.Handlandmark.PINKY_TIP]

    #THUMBS UP JIKA HANYA JEMPOL YG DI ANGKAT
    if (ujung_jempol.y < ujung_telunjuk.y and
        ujung_jempol.y < ujung_tengah.y and
        ujung_jempol.y < ujung_manis.y and
        ujung_jempol.y < ujung_kelingking.y):
        return "Mantap"
    
    return "lu ngapain ege"
    
#untuk mendeteksi tangan pake mediapipe
def detect_hand_gesture(image,hand):
    image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    results = hand.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    return image

cap = cv2.VideoCapture(0)

if cap.isOpened():
    print("camera gk bisa dibuka")
    exit()

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        print("gagal menangkap frame")
        break

    frame = detect_hand_gesture(frame,hands)


    cv2.imshow("handgesture dgn opencv dan mediapipe", frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()