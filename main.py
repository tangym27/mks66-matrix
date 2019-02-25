from display import *
from draw import *
from matrix import *
from random import randint
import math
screen = new_screen()

matrix = new_matrix(4,10)
m1 = [[1, 2, 3, 1], [4, 5, 6, 1]]
m2 = [[2, 4], [4, 6], [6, 8]]

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
print("Printing matrix:")
print("==========================")
print_matrix(A)
print_matrix(B)

print("Printing matrix after multiplication:")
print("==========================")
matrix_mult(A,B)
print_matrix(B)

print("Printing matrix after ident:")
print("==========================")
A = ident(A)
print_matrix(A)

#####################################################################################################################
#just doing this because i didnt want to code too many things haha
#black bars in the top and bottom (game is more rectangle than square)
black = [0,0,0]
color = black
heading = new_matrix()
footer = new_matrix()
i = 0
while ( i < 101 ):
    add_point(footer, 0, 500-i)
    add_point(footer, 500, 500-i)
    add_point(heading, 0, 100-i)
    add_point(heading, 500, 100-i)
    i += 1
draw_lines(heading, screen, color)
draw_lines(footer, screen, color)
#######################################
#makes the ground
block = new_matrix()
i = 0
while (i < 30):
    add_point(block, 0, 120-i)
    add_point(block, 500, 120-i)
    i += 1
draw_lines(block, screen, [ 230, 100, 25 ])
#######################################
#makes the lines in the ground
lines = new_matrix()
j = 0
i = 1
while (j < 500 ):
    if (i%2):
        add_edge(lines, j, 0, 0, j , 120, 0)
        add_edge(lines, j, 107, 0, j+10, 107, 0)
        add_edge(lines, j+10, 0, 0, j+10, 120, 0)
        j += 10
    else:
        add_edge(lines, j, 0, 0, j, 120, 0)
        add_edge(lines, j+25, 0, 0,  j+25, 120, 0)
        j += 25
    i +=1
draw_lines(lines, screen, black)
#######################################
#such bad code, sets up all of the elements, edges are the outline of each element (right and left side)
i = 0
angle = 2 * math.pi / 360
center= 145

grass = new_matrix()
edge = new_matrix()
edge2 = new_matrix()

grass2 = new_matrix()
edge3 = new_matrix()
edge4 = new_matrix()

grass3 = new_matrix()
edge0 = new_matrix()
edge1 = new_matrix()

cloud = new_matrix()
edge5 = new_matrix()
edge6 = new_matrix()

cloud2 = new_matrix()
edge7 = new_matrix()
edge8 = new_matrix()

circle = new_matrix()
edge9 = new_matrix()

while (i < 20):
#grasses of randomized length
    r = randint(20,40 -i) -i
    r1 = randint(20,40 -i) -i
    add_edge(grass, 300-r, 120+i, 0, 300+r, 120+i, 0)
    add_point(edge, 300-r-1,120+i)
    add_point(edge2, 300+r+1,120+i)

    add_edge(grass2, 60-r1, 120+i, 0, 60+r1, 120+i, 0)
    add_point(edge3, 60-r1-1,120+i)
    add_point(edge4, 60+r1+1,120+i)

#green hill (top curve and ..lump)
    for n in range(180):
        angle = (n * 2 * math.pi )/ 360
        dx = int(i * math.cos(angle))
        dy = int(i * math.sin(angle))
        if (i == 19):
            add_edge(edge9, center+dx, center + dy, 0, center + dx+1, center +dy+1, 0)
        else:
            add_edge(circle, center+dx, center + dy, 0, center + dx+1, center +dy+1, 0)

    if (i < 15):
        add_edge(grass3, 112+i, 119+i+i, 0, 179-i, 119+i+i, 0)
        add_edge(grass3, 112+i, 120+i+i, 0, 179-i, 120+i+i, 0)
        add_point(edge0, 112+i, 119+i+i)
        add_point(edge1, 179-i, 119+i+i)
        add_point(edge0, 112+i, 120+i+i)
        add_point(edge1, 179-i, 120+i+i)

#clouds which i was told are just the bushes?!
    cloud_height = 335+i
    add_edge(cloud, 140-r, cloud_height, 0, 140+r, cloud_height, 0)
    add_point(edge5, 140-r-1,cloud_height)
    add_point(edge6, 140+r+1,cloud_height)

    cloud_height2 = 310+i
    add_edge(cloud2, 360-r1, cloud_height2, 0, 360+r1, cloud_height2, 0)
    add_edge(cloud2, 390-r1, cloud_height2, 0, 390+r1, cloud_height2, 0)
    add_edge(cloud2, 420-r1, cloud_height2, 0, 420+r1, cloud_height2, 0)
    add_point(edge7, 360-r1-1,cloud_height2)
    add_point(edge8, 420+r1+1,cloud_height2)

    i+=1

#semi-circle of the green hill
draw_lines( circle, screen, [5,161,4] )
draw_lines( edge9, screen, black )

#bush1
draw_lines(grass, screen, [189,254,24])
draw_lines(edge, screen, black)
draw_lines(edge2, screen, black)

#bush2
draw_lines(grass2, screen, [189,254,24])
draw_lines(edge3, screen, black)
draw_lines(edge4, screen, black)

#green hill
draw_lines(grass3, screen, [5,161,4])
draw_lines(edge0, screen, black)
draw_lines(edge1, screen, black)

#cloud1
draw_lines(cloud, screen, [251,253,252])
draw_lines(edge5, screen, black)
add_edge(edge6, 120 , 335, 0, 160, 335, 0)
draw_lines(edge6, screen, black)

#cloud2
draw_lines(cloud2, screen, [251,253,252])
draw_lines(edge7, screen, black)
add_edge(edge8, 340 , 310, 0, 440, 310, 0)
draw_lines(edge8, screen, black)


#######################################
# makes that really long four block road
b = new_matrix()
b1 = new_matrix()
b2 = new_matrix()
i = 0
count = 0
for j in range(6):
    i = 0
    while (i <20):
        height = 190+i
        add_edge(b, 180, height, 0, 200 + count, height, 0)
        if ((i%5)== 0):
            r = randint(4,16)
            add_edge(b1, 180, height, 0 , 200+count, height, 0)
            add_edge(b2, 180+count+r, height, 0, 180+count+r, height+5, 0)
        i += 1
    add_edge(b2, 200+count, 190, 0, 200+count, 210, 0)
    count += 20
add_edge(b2, 180, height+1, 0 , 300, height+1, 0)
add_edge(b1, 180, 190, 0, 180, height, 0)
draw_lines(b, screen, [179,91,49])
draw_lines(b1, screen, black)
draw_lines(b2, screen, black)

#######################################
#makes the pipe!
pipe = new_matrix()
edge = new_matrix()
edge2 = new_matrix()

add_edge(edge, 455, 154, 0, 415 , 154, 0)
add_edge(edge, 455, 155, 0, 415 , 155, 0)
add_edge(edge, 455, 170, 0, 415 , 170, 0)
add_edge(edge, 455, 171, 0, 415 , 171, 0)
i = 0
while (i < 50):
    startx = 450
    endx = 420
    y = 120+ i
    if (i <= 33):
        add_edge(pipe, startx, y, 0, endx, y, 0)
        add_point(edge, startx, y)
        add_point(edge2, endx,y)
        add_point(edge, startx+1, y)
        add_point(edge2, endx-1,y)
    else:

        add_edge(pipe, startx+5, y, 0, endx-5, y, 0)
        add_point(edge, startx+5, y)
        add_point(edge, startx+6, y)
        add_point(edge2, endx-6,y)
        add_point(edge2, endx-5,y)
    i += 1

draw_lines(pipe, screen, [122,206,14])
draw_lines(edge, screen, black)
draw_lines(edge2, screen, black)

#######################################
#makes the first block
b = new_matrix()
b1 = new_matrix()
b2 = new_matrix()

i = 0
while (i <20):
    height = 190+i
    add_edge(b, 100, height, 0, 120 , height, 0)
    if ((i%5)== 0):
        r = randint(3,17)
    i += 1
add_edge(b1, 100, 190, 0, 100, 210, 0)
add_edge(b1, 100, 210, 0, 120, 210, 0)
add_edge(b1, 100, 190, 0, 120, 190, 0)
add_edge(b1, 120, 190, 0 , 120, 210, 0)

draw_lines(b, screen, [204,78,12])
draw_lines(b1, screen, black)

#######################################
#makes the highest block
b = new_matrix()
b1 = new_matrix()
b2 = new_matrix()

i = 0
while (i <20):
    height = 260+i
    add_edge(b, 230, height, 0, 250 , height, 0)
    i += 1
add_edge(b1, 230, 260, 0, 230, height, 0)
add_edge(b1, 250, 260, 0, 250, height, 0)
add_edge(b1, 230, 260, 0, 250, 260, 0)
add_edge(b1, 230, height, 0 , 250, height, 0)

draw_lines(b, screen, [204,78,12])
draw_lines(b1, screen, black)
#######################################

display(screen)
save_extension(screen, 'img.png')
