from p5 import *
from PIL import Image


img = Image.open('face.jpg')
px = img.load()

W = img.size[0]
H = img.size[1]
r = 10
scale = 1

def setup():
        size(scale*W, scale*H)
        no_stroke()
        rect_mode("CENTER")

def draw():
        #background(0)
        x = mouse_x
        y = mouse_y

        n = 25
        '''for i in range(-n, n):
                for j in range(-n, n):
                        # color_mode('RGB', px[i, j][0], px[i, j][1], px[i, j][2], 255)'''

        pixel = px[int(x)%W, int(y)%H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x, mouse_y), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x + 2, mouse_y), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x + 2, mouse_y + 2), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x , mouse_y+2), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x - 2, mouse_y - 2), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x + 2, mouse_y - 2), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x + 2, mouse_y - 2), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x + 4, mouse_y - 4), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x - 4, mouse_y - 2), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x - 5, mouse_y - 5), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x - 7, mouse_y - 7), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x - 9, mouse_y - 5), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x + 11, mouse_y - 7), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x - 7, mouse_y - 7), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x - 8, mouse_y - 1), r)

        pixel = px[int(x) % W, int(y) % H]
        fill(pixel[0], pixel[1], pixel[2])
        circle((mouse_x + 8, mouse_y - 4), r)


if __name__ == '__main__':
        run()


