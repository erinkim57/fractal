from PIL import Image, ImageDraw

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

# MAX_ITER = 10
MAX_ITER = 50
width = 600
height = 400

RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

a = Image.new("HSV", (width, height), (0, 0, 0))
draw = ImageDraw.Draw(a)

for x in range(width):
    for y in range(height):
        c = complex(RE_START + (x/ width) * (RE_END - RE_START),
        IM_START + (y/ height) * (IM_END - IM_START))
        m = mandelbrot(c)
        # hue = int(255 * m / MAX_ITER)
        hue = 30 - int(25 * 2*m / MAX_ITER)
        saturation = 255
        value = 255 if m < MAX_ITER else 0
        draw.point ([x,y], (hue, saturation, value))

a.convert("RGB")
a.show()