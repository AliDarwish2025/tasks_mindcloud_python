from PIL import Image

img_path = Image.open("E:/صوري/IMG_20190619_151138.jpg")  

width, height = img_path.size

img_path = img_path.convert("RGB")

pixels = img_path.load()

for x in range(width // 4):       
    for y in range(height):       
        pixels[x, y] = (0, 0, 0)  

img_path.show()

