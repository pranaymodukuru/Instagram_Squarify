import os
import sys
import argparse
from PIL import Image, ImageFilter, ImageEnhance

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--images_path', default = './pictures/', help='The folder containing pictures to be modified')
    parser.add_argument('--destination_path', default = './output_files/', help='The folder the results are stored in')
    parser.add_argument('--width', default=1080, type=int, help='Width of output image')
    parser.add_argument('--height', default=1080, type=int, help='Height of output image')
    parser.add_argument('--blur_strength', default=100, type=int, help='Background blur amount')
    parser.add_argument('--background_brightness', default=0.8, type=float, help='Background Brightness')

    args = parser.parse_args()

    print(args.background_brightness)

    img_folder = args.images_path
    dest_folder = args.destination_path

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for filename in os.listdir(img_folder):
        img = Image.open(f'{img_folder}{filename}')
        name = os.path.splitext(filename)[0]
        img.thumbnail((1080, 1080), Image.ANTIALIAS)

        height = img.size[1]
        width = img.size[0]
        bg_width = args.width
        bg_height = args.height

        landscape = True
        if width >= 1080:
            if height >= 850:
                bg_height = 1080
            elif 566 <= height < 850:
                bg_height = height + 200
            elif height < 566:
                bg_height = 566
        else:
            landscape = False
            if width >= 850:
                bg_width = 1080
            elif 566 <= width < 850:
                bg_width = width + 200
            elif width < 566:
                bg_width = 566

        bg = img
        enhancer = ImageEnhance.Brightness(bg)
        bg = enhancer.enhance(args.background_brightness)

        if landscape:
            bg = bg.resize((bg_width, bg_height)).filter(ImageFilter.GaussianBlur(radius=args.blur_strength))
            mid = int(bg.size[1]/2)
            span = int(round(img.size[1]/2))
            bg.paste(img, (0, mid-span))
        else:
            bg = bg.resize((bg_width, bg_height)).filter(ImageFilter.GaussianBlur(radius=args.blur_strength))
            mid = int(bg.size[0]/2)
            span = int(round(img.size[0]/2))
            bg.paste(img, (mid-span, 0))

        bg.save(f'{dest_folder}{name}.jpg', 'JPEG')
