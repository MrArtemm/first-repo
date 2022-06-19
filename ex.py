import cv2
from PIL import Image

image_path = 'cat.jpeg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
cat = Image.open(image_path)
chain = Image.open('chain.png')
cat = cat.convert('RGBA')
chain = chain.convert('RGBA')
for (x, y, w, h) in cat_face:
    chain = chain.resize((w, h//2))
    cat.paste(chain, (x, y + h//5), chain)
    cat.save('cat_chain.png')

