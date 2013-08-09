from mat import Mat
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels
    equal to {'x','y','u'}.  So you should write your procedure as if
    it were defined 'def identity(labels):'.  However, if you want the labels of
    your identity matrix to be {'x','y','u'}, you can just call
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).
    '''
    return Mat((labels, labels), {(i,i):1 for i in labels})

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    base = identity()
    base.f[('x','u')] = x
    base.f[('y','u')] = y
    return base

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    base = identity()
    base.f[('x','x')] = a
    base.f[('y','y')] = b
    return base

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    base = identity()
    base.f[('x','x')] = math.cos(angle)
    base.f[('x','y')] = -math.sin(angle)
    base.f[('y','x')] = math.sin(angle)
    base.f[('y','y')] = math.cos(angle)
    return base

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return translation(x, y) * rotation(angle) * translation(-x, -y)

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    base = identity()
    base.f[('x','x')] = -1
    return base

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    base = identity()
    base.f[('y','y')] = -1
    return base

## Task 8
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    base = identity({'r','g','b'})
    base.f[('r','r')] = scale_r
    base.f[('g','g')] = scale_g
    base.f[('b','b')] = scale_b
    return base

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    base = identity({'r','g','b'})
    scale_r = 77/256
    scale_g = 151/256
    scale_b = 28/256
    base.f[('r','r')] = scale_r
    base.f[('r','g')] = scale_g
    base.f[('r','b')] = scale_b
    base.f[('g','r')] = scale_r
    base.f[('g','g')] = scale_g
    base.f[('g','b')] = scale_b
    base.f[('b','r')] = scale_r
    base.f[('b','g')] = scale_g
    base.f[('b','b')] = scale_b
    return base

## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    pass


