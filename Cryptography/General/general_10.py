from PIL import Image, ImageChops
im1 = Image.open(r"lemur.png") .convert("RGB")
im2 = Image.open(r"flag.png") .convert("RGB")
im3 = ImageChops.difference(im1, im2)
im3.show()
