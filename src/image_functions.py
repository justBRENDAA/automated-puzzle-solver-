import cv2
import numpy as np

def split_image(image, num_rows, num_cols):
    tiles = []
    h, w = image.shape[:2]
    tile_height = h // num_rows
    tile_width = w // num_cols
    
    for row in range(num_rows):
        for col in range(num_cols):
            top = row * tile_height
            bottom = (row + 1) * tile_height if row != num_rows - 1 else h
            left = col * tile_width
            right = (col + 1) * tile_width if col != num_cols - 1 else w
            
            tile = image[top:bottom, left:right]
            tiles.append(tile)

    return tiles