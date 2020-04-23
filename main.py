import cv2
import numpy as np
import operator

image = cv2.imread('./images/checkerboard.jpg')

# print(image.shape)
rows, cols, _ = image.shape

# BFS Algorithm
visited = [[False for j in range(cols)] for i in range(rows)]
starting_pixel = (63, 191)
visited[starting_pixel[0]][starting_pixel[1]] = True
queue = []
queue.append(starting_pixel)

directions = [(1,0), (-1,0), (0,1), (0,-1)]

while(len(queue) != 0):
	found = False
	current_pixel = queue.pop(0)
	# print(len(queue))
	for d in directions:
		new_pixel = tuple(map(operator.add, current_pixel, d))
		# print(new_pixel)
		if(not visited[new_pixel[0]][new_pixel[1]] and np.all(image[current_pixel] == image[new_pixel])):
			found = True
			queue.append(new_pixel)
			visited[new_pixel[0]][new_pixel[1]] = True

	if(not found):
		image[current_pixel] = [0,0,255]
	

cv2.imshow('lol', image)
cv2.waitKey(0)

# for i in range(rows):
# 	for j in range(cols):
# 		print(image[i,j], end='')
# 	print()