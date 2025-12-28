from PIL import Image

def open_image(path):
    img = Image.open(path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    return img
