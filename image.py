from PIL import Image
from PIL.ImageOps import invert
from io import BytesIO
from typing import List

def binToImage(file) -> Image.Image:
    with BytesIO() as image:
        file.save(image)
        try:
            i = Image.open(image)
            i.load()
            return i
        except:
            return None

def validate(file) -> bool:
    if file is None: 
        return False
    image = binToImage(file)
    return image

def ratio_image(image: Image.Image) -> Image.Image:
    COURIER_RATIO = 6/10 # a character is about 60% as wide as it is tall in Courier New
    width, height = image.size
    return image.resize((width, int(height*COURIER_RATIO)))

ASCIILines = List[str]
def processImage(image: Image.Image) -> ASCIILines:
    im = ratio_image(image)
    shrunk_image = invert(
        im.resize(
            (100, int(im.height*(100/im.width)))
        ).convert("L")
    )

    BOXES = "░▒▓█"
    converted = shrunk_image.getdata()
    converted = [
        BOXES[max(0, int(len(BOXES)*i/255)-1)] for i in converted
    ]
    return [
        "".join(converted[100*i:100*(i+1)]) for i in range(len(converted)//100)
    ]

