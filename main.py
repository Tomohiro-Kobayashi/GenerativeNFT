import os 
import glob
import cv2
import itertools
from PIL import Image, ImageDraw, ImageFilter

class ImagesGNFT:
    def __init__(self, images_pass="./images"):
        self.images_pass = images_pass
        self.list_images_parts_pass = []
        self.list_all_combination_parts = []


    def read_image_parts_pass(self):
        list_images_pass = sorted(glob.glob(self.images_pass + '/*'))
        for parts_pass in list_images_pass:
            self.list_images_parts_pass.append(glob.glob(parts_pass + '/*')) 
        

    def make_combination_images_pass(self):
               
        self.list_all_combination_parts = list(itertools.product(
            self.list_images_parts_pass[0],
            self.list_images_parts_pass[1],
            self.list_images_parts_pass[2],
            self.list_images_parts_pass[3],
            self.list_images_parts_pass[4],
            self.list_images_parts_pass[5],
            self.list_images_parts_pass[6],))


    def make_combination_images(self):
        img = 0
        name = 0
        for image_pass in self.list_all_combination_parts:  
            bg_img = Image.open(image_pass[0]).convert('RGBA')
            for im in range(len(image_pass)-1):       
                paste_img = Image.open(image_pass[im+1]).convert('RGBA')
                bg_img.paste(paste_img, (0, 0), paste_img)
            name += 1
            bg_img.save("Output/" + str(name) + "sample.png")
            

def main():
    img_pass = ImagesGNFT()
    img_pass.read_image_parts_pass()
    img_pass.make_combination_images_pass()
    img_pass.make_combination_images()
    


if __name__ == "__main__":
    main()

