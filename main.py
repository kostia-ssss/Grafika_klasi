from PIL import Image

class ImageEditor():
    def __init__(self , file_name_original , file):
        with Image.open(file_name_original) as file:
            self.file_name_original = file_name_original
            self.file = file
    def save_image(self , name):
        with Image.open(self.file_name_original) as image:
            image.save(name + '.jpg')
    def make_photo_black_white(self):
        with Image.open(self.file_name_original) as file:
            file = file.convert('L')
            file.save("b_w.jpg")

with Image.open('photo_2024-11-29_18-24-12.jpg') as file:
    file_ = file
img = ImageEditor('photo_2024-11-29_18-24-12.jpg' , file_)
img.make_photo_black_white()
img.save_image('efgy')