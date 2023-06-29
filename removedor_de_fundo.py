from rembg import remove
from PIL import Image

img = Image.open('img.jpg')

img_without_back = remove(img)

img_without_back.save('img_without_back.png')
