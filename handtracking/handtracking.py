import cv2
import mediapipe as mp

from handtracking.helpers.webcam import webcam

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands()


def bgr2rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def using_hand_landmarks(image, func):
    processed_hands = hands.process(bgr2rgb(image))
    hand_landmarks = processed_hands.multi_hand_landmarks

    if hand_landmarks:
        for hand in hand_landmarks:
            func(image, hand)


def draw_hand(image, hand):
    mp_draw.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)


def dotted_hand(image):
    using_hand_landmarks(image, draw_hand)
    return image


webcam(dotted_hand, show_fps=True)
