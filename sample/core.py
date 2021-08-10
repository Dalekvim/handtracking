import cv2
import mediapipe as mp
import numpy as np

from sample.helpers import video

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
draw = mp.solutions.drawing_utils


def bgr2rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def dotted_hand(image):
    processed_hands = hands.process(bgr2rgb(image))
    hand_landmarks = processed_hands.multi_hand_landmarks

    if not hand_landmarks:
        return image

    for hand in hand_landmarks:
        draw.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)

    return image


video(dotted_hand, show_fps=True)
