import os.path

from pdf2image import convert_from_path
from PIL import Image
from itertools import product

def pdf_to_page(pdf_file):
    '''transform pdf_file to individual pages'''
    pages = convert_from_path(pdf_file)
    count = 1
    for page in pages:
        if count%2 == 0:
            count = count
            page.save("assets/pages/out_" + str(count - 1) + "_verso.jpg", 'JPEG', poppler_path="/usr/local/Cellar/poppler")
            print("page saved:" + str(count) + "_VERSO")
            count = count + 1
        else:
            page.save("assets/pages/out_" + str(count) + "_recto.jpg", 'JPEG', poppler_path="/usr/local/Cellar/poppler")
            print("page saved:" + str(count) + "_RECTO")
            count = count + 1


def split_page_singles(image):
    '''split page containing image in singles.'''
    infile = image

    img = Image.open(infile)
    width, height = img.size

    # split image evenly in 4 quadrants.
    chopW = int(width / 2)
    chopY = int(height / 2)

    file = 1

    # Save Chops of original image
    for x0 in range(0, width, chopW):
        for y0 in range(0, height, chopY):
            box = (x0, y0,
                   x0 + chopW if x0 + chopW < width else width - 1,
                   y0 + chopY if y0 + chopY < height else height - 1)
            print('%s %s' % (infile, box))
            img.crop(box).save("assets/singles/"+str(file)+".jpg")
            file += 1


split_page_singles('assets/pages/out_1_verso.jpg')





