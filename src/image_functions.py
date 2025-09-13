import cv2
import numpy as np
import matplotlib.pyplot as plt

def split_image(image, rows, cols):
    h, w = image.shape[:2]
    print("height: ", h)
    print("width: ", w)

    slice_height = h//rows
    slice_width = w//cols

    print("slice height: ", slice_height) 
    print("slice width: ", slice_width)
    print()

    slices = []

    for row in range(rows):
        for col in range(cols):
            print(f"Slice: {row, col}")

            height_start = row * slice_height
            height_end =  (row + 1) * slice_height if row < rows - 1 else h  

            width_start = col * slice_width
            width_end =  (col + 1) * slice_width if col < cols - 1 else w

            print(f"Height slice values: {height_start} : {height_end}")
            print(f"Width slice values: {width_start} : {width_end}")
            print()

            slice = image[height_start:height_end, width_start:width_end]
            plt.imshow(slice)
            plt.axis("off")
            plt.show()