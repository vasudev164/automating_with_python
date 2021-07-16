from PIL import Image


filename = r"C:\Users\asus\Downloads\U19CS095 DCOM PRACTICAL 7 AWGN EFFECT ON MODULATION_8.jpg"
img = Image.open(filename)
w, h = img.size

for i in range(120):
    for j in range(450):
        r, g, b = img.getpixel((i, j))
        if r>165 or g>165 or b>165:
            img.putpixel((i, j), (180, 180, 180, 0))

img.save(r"C:\Users\asus\Pictures\U19CS095 DCOM PRACTICAL 7 AWGN EFFECT ON MODULATION_8_New.jpg")
