import numpy as np
import math
import cmath
import PIL.Image as im
def f(x):
    return x**3-1

def fprime(x):
    return 3*x**2

def newtonsMethod(x):
    for i in range(100):
        x = x-f(x)/fprime(x)
    return x
def grid_gen(x1,x2,y1,y2,x_res=100,y_res=100):
    xs=np.linspace(x1,x2,x_res)
    ys=np.linspace(y1,y2,y_res)
    return xs[:,None] +1j*ys

def newton_method(x1,x2,y1,y2,x_res=100,y_res=100):
    grid = grid_gen(x1,x2,y1,y2,x_res,y_res)
    grid=newtonsMethod(grid)
    return grid

def classify(x):
    x0=1
    x1=-0.5+(np.sqrt(3)/2)*1j
    x2=-0.5-(np.sqrt(3)/2)*1j
    if cmath.isclose(x,x0):
        return(255,0,0)
    if cmath.isclose(x,x1):
        return (0,255,0)
    if cmath.isclose(x,x2):
        return (0,0,255)
    else:
        return (0,0,0)

def image_make(grid,x_res,y_res):
    pixels = np.transpose(np.array(np.vectorize(lambda x:classify(x))(grid)),axes=(2,1,0)).astype('uint8')
    img = im.fromarray(pixels, mode='RGB')
    img.show()

def main():
    x_res = 1024
    y_res = 1024
    x1=-2
    x2=2
    y1=-2
    y2=2
    grid= newton_method(x1,x2,y1,y2,x_res,y_res)
    image_make(grid,x_res,y_res)

if __name__ == '__main__':
    main()