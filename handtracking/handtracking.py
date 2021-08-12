from numpy import ndarray

from helpers.using_hand_landmarks import using_hand_landmarks
from helpers.mp_modules import mp_hands, mp_draw
from helpers.webcam import webcam


def draw_hand(image: ndarray, hand) -> None:
    """
    This is a process that modifies the image by drawing a network representing the input hand landmark.

    :param image: This input image as a numpy array.
    :param hand: Landmark for a single hand.
    :return: None.
    """
    mp_draw.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)


def dotted_hand(image):
    """
    This applies the draw_hand function to an image and the landmarks.

    :param image: The image that you want the landmarks drawn on.
    :return: None.
    """
    using_hand_landmarks(image, draw_hand)
    return image


if __name__ == "__main__":
    webcam(dotted_hand, show_fps=True)
