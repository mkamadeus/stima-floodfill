import cv2
import numpy as np
import operator
import random

image = cv2.imread('./images/checkerboard.jpg')
rows, cols, _ = image.shape
tolerance = 0
sampling_radius = 0


def is_pixel_valid(r, c):
    return (r >= 0 and c >= 0 and r < rows and c < cols)


def generate_color(prev_color):
    red, green, blue = (random.randint(0, 255) + prev_color[0])/2, (random.randint(
        0, 255) + prev_color[1])/2, (random.randint(0, 255) + prev_color[2])/2

    return [red, green, blue]


print('Image size:', str(rows) + ", " + str(cols))
print('Tolerance:', tolerance)
print('Sampling Radius:', sampling_radius)

# BFS Algorithm
visited = [[False for j in range(cols)] for i in range(rows)]

starting_pixel = (0, 127)
sample_average_list = np.asarray([])
for i in range(-sampling_radius, sampling_radius+1):
    for j in range(-sampling_radius, sampling_radius+1):
        r, c = starting_pixel
        if(is_pixel_valid(r + i, c + j)):
            sample_average_list = np.append(
                sample_average_list, np.mean(image[(r + i, c + j)])
            )

starting_pixel_mean = np.mean(sample_average_list)

visited[starting_pixel[0]][starting_pixel[1]] = True
queue = []
queue.append(starting_pixel)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

prev_color = [0, 0, 255]
cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Result', 900, 900)
cv2.imshow('Result', image)
cv2.waitKey(0)
while(len(queue) != 0):
    found = False
    current_pixel = queue.pop(0)
    for d in directions:
        new_pixel = tuple(map(operator.add, current_pixel, d))
        if(is_pixel_valid(new_pixel[0], new_pixel[1])):
            new_pixel_mean = np.mean(image[new_pixel])
            if(not visited[new_pixel[0]][new_pixel[1]] and starting_pixel_mean - tolerance <= new_pixel_mean <= starting_pixel_mean + tolerance):
                found = True
                queue.append(new_pixel)
                visited[new_pixel[0]][new_pixel[1]] = True

    image[current_pixel] = [0, 0, 200]
    cv2.imshow('Result', image)
    cv2.waitKey(1)

print('Floodfill complete!')
cv2.imshow('Result', image)
cv2.waitKey(0)

# cv2.imwrite('./result/gradient_small_128.jpg', image)
