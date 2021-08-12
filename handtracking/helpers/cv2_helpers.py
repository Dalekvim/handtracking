import cv2
from numpy import ndarray


def bgr2rgb(image: ndarray):
    """
    Converts image from BGR to RGB format.

    :param image: The image as a numpy array.
    :return: The image in RGB format.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
