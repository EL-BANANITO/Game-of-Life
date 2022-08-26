import pygame
import keyboard
import time

black = (0, 0, 0)
white = (255, 255, 255)#RGB colors
red = (255, 0, 0)

WIDTH = 10
HEIGHT = 10
MARGIN = 1
cube_count = 72
grid = []
for row in range(cube_count):
    grid.append([])
    for column in range(cube_count):
        grid[row].append(0)
grid[1][5] = 0#1 draw cube 0 delete or not draw the cube
pygame.init()
window_size = [793, 793]
scr = pygame.display.set_mode(window_size)
pygame.display.set_caption("Grid")
done = False
clock = pygame.time.Clock()
cords = []  # list of all possible coordinates
for i in range(72):
    for j in range(72):
        cords.append([i, j])#get all possible coordinates of cubes
coordinates = []
x_cord = []
y_cord = []
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
            if [row, column] not in coordinates:
                coordinates.append([row, column])
                x_cord.append(column)
                y_cord.append(row)
                print(f'coordinates list:{coordinates}')
    scr.fill(black)
    for row in range(cube_count):
        for column in range(cube_count):
            color = white
            if grid[row][column] == 1:
                color = red
            pygame.draw.rect(scr,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    clock.tick(50)
    pygame.display.flip()

    if keyboard.is_pressed('space'):#after space will be pressed game will start
        #time.sleep(0.01)
        index = []
        for i in coordinates:#get all live cubes coordinate indexes of list cords
            index.append(cords.index(i))

        for j in index:#spawn(draw) cubes
            near_count = 0
            if j - 1 in index:
                near_count += 1
            if j + 1 in index:
                near_count += 1
            if j - 72 in index:
                near_count += 1
            if j + 72 in index:
                near_count += 1
            if j - 71 in index:
                near_count += 1
            if j + 71 in index:
                near_count += 1
            if j - 73 in index:
                near_count += 1
            if j + 73 in index:
                near_count += 1
            if near_count != 2 and near_count != 3:#if cube don't have 2 or 3 neighborhood cube will die(delete)
                grid[cords[j][0]][cords[j][1]] = 0
                coordinates.remove([cords[j][0], cords[j][1]])

        index_all = []
        for i in cords:#get all indexes of coordinate in list cords
            index_all.append(cords.index(i))

        for j in index_all:#killing(erase) cubes
            near_count = 0
            if j - 1 in index:
                near_count += 1
            if j + 1 in index:
                near_count += 1
            if j - 72 in index:
                near_count += 1
            if j + 72 in index:
                near_count += 1
            if j - 71 in index:
                near_count += 1
            if j + 71 in index:
                near_count += 1
            if j - 73 in index:
                near_count += 1
            if j + 73 in index:
                near_count += 1
            if near_count == 3:#if an empty cube has 3 neighborhoods, then a new cube will be drawn
                grid[cords[j][0]][cords[j][1]] = 1
                coordinates.append([cords[j][0], cords[j][1]])
                x_cord.append(cords[j][1])
                y_cord.append(cords[j][0])

    if keyboard.is_pressed('D'):#after key D will be pressed all cubes will be deleted
        coordinates = []
        for i in x_cord:
            for j in y_cord:
                grid[j][i] = 0
        x_cord = []
        y_cord = []

pygame.quit()
