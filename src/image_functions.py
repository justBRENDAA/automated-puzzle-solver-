import cv2
import numpy as np

def split_image(image, num_rows, num_cols):
    tiles = []
    h, w = image.shape[:2]
    tile_height = h // num_rows
    tile_width = w // num_cols
    
    # return tiles