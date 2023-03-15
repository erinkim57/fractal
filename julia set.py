from PIL import Image, ImageDraw

def julia(c, z0):
    z = z0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

MAX_ITER = 30
width = 666
height = 400

RE_START = -2
RE_END = 2
IM_START = -1.2
IM_END = 1.2

# c = complex(0.285, 0.01)
c = complex(0.543,0.007)

a = Image.new("HSV", (width, height), (0, 0, 0))
draw = ImageDraw.Draw(a)

for x in range(width):
    for y in range(height):
        z0 = complex(RE_START + (x/ width) * (RE_END - RE_START),
        IM_START + (y/ height) * (IM_END - IM_START))
        m = julia(c, z0)
        # hue = int(255 * m / MAX_ITER)
        hue = int (350 * 1.5*m / MAX_ITER)
        saturation = 255
        value = 255 if m < MAX_ITER else 0
        draw.point ([x,y], (hue, saturation, value))

a.convert("RGB")
a.show()