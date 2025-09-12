import cv2
import numpy as np

def split_image(image, rows, cols):
    h, w = image.shape[:2]
    print("height: ", h)
    print("width: ", w)

    slice_height = h//rows
    slice_width = w//cols

    print("slice height: ", slice_height)
    print("slice width: ", slice_height)

