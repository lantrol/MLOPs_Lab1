from PIL import Image
import random

from .model import ImageModel


def predict_image(image):
    model = ImageModel()
    return model.predict(image)


def resize_image(image, width: int, height: int):
    image = image.resize((width, height))
    return image.size


if __name__ == "__main__":
    image = Image.open("samples/hamis.jpg")
    image = resize_image(image, 32, 32)

    random.seed(1)
    print(predict_image(image))
    random.seed(2)
    print(predict_image(image))
    random.seed(3)
    print(predict_image(image))
