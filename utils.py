import numpy as np
import cv2

colors = {
    'yellow' : (0, 255, 255),
    'red': (0, 0, 255),
    'green': (0, 255, 0),
    'blue': (255, 0, 0),
    'magenta': (255, 0, 255)
}

def get_color_representation(color: str):
    """
    Gives the BGR representation of a color input as string.
    
    Args:
        color (str): the color name
    
    Returns:
        (int, int, int) : the representation of the given color in BGR color space
    """
    return colors.get(color)


def get_limits(color, tol=10):
    """
    Transform a given color in BGR space to HSV equivalent. Returns a lower and an upper limit around the color in HSV
    space. The width of the range is control by tol param.

    Args:
        color (ArrayLike) : A color in BGR color space
        tol (int) : The tolerance around the exact value of the corresponding Hue in the HSV color space.

    Returns:
        (numpy.ndarray, numpy.ndarray) : lower limit and upper limit in HSV color space.
    """

    placeholder = np.uint8([[color]])
    hsvColor = cv2.cvtColor(placeholder, cv2.COLOR_BGR2HSV)

    lowerLimit = max(hsvColor[0, 0, 0] - tol, 0), 100, 100
    upperLimit = min(hsvColor[0, 0, 0] + tol, 180), 255, 255

    return np.array(lowerLimit, dtype=np.uint8), np.array(upperLimit, dtype=np.uint8)
