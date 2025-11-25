import os
import random

class ImageModel():
    def __init__(self):
        self.class_names = ["Car", "Motorcicle", "Plane", "Helicopter"]
        self.num_classes = len(self.class_names)

    def predict(self, image) -> str:
        return random.choice(self.class_names)
