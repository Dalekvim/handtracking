from numpy import ndarray

from .cv2_helpers import bgr2rgb
from .mp_modules import mp_hands

hands = mp_hands.Hands()


def using_hand_landmarks(image: ndarray, func):
    """
    Modifies the image using the input function and hand landmarks.

    :param image: The image as a numpy array.
    :param func: The function to be applied to the image and a hand landmark.
    :return: None.
    """
    processed_hands = hands.process(bgr2rgb(image))
    hand_landmarks = processed_hands.multi_hand_landmarks

    if hand_landmarks:
        for hand in hand_landmarks:
            # This loop iterates through all the hands landmarks detected in the image.
            # The function is applied to an image as a numpy array and a hand landmark.
            func(image, hand)
