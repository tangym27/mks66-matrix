"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    cols = len(matrix)
    rows = len(matrix[0])
    line = ""
    for row in range(rows):
        for col in range(cols):
            line += str(matrix[col][row]) + '  '
        line += "\n"
    print line


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    matrix = new_matrix()
    for c in range( 4 ):
        for r in range( 4 ):
            if (c == r):
                matrix[c][r] = 1
    # print_matrix(matrix)
    return matrix

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    rows = 4
    cols = len(m2)
    new_mat = new_matrix(rows, cols)
    for row in range(rows):
        for col in range(cols):
            product = 0
            for i in range(len(m1)):
                product += (m1[i][row] * m2[col][i])
            m2[col][row] = product
#    m2 = new_mat
    # return m2

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
