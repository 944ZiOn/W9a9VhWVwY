# 代码生成时间: 2025-10-18 14:44:12
import numpy as np
from PIL import Image
import os
import glob

"""
Image Resizer Batch: A script to batch resize images to a specified size.
Usage:
    python image_resizer_batch.py <source_folder> <target_folder> <new_width> <new_height>"""

def resize_image(image_path, target_path, new_width, new_height):
    """
    Resize a single image.
    :param image_path: Path to the original image.
    :param target_path: Path to save the resized image.
    :param new_width: New width for the resized image.
    :param new_height: New height for the resized image.
    """
    try:
        with Image.open(image_path) as img:
            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(target_path)
            print(f"Resized image saved to {target_path}")
    except IOError as e:
        print(f"Error resizing image {image_path}: {e}")


def batch_resize_images(source_folder, target_folder, new_width, new_height):
    """
    Batch resize images in a folder.
    :param source_folder: Path to the folder containing images to resize.
    :param target_folder: Path to the folder where resized images will be saved.
    :param new_width: New width for the resized images.
    :param new_height: New height for the resized images.
    """
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for image_path in glob.glob(os.path.join(source_folder, "*")):
        filename = os.path.basename(image_path)
        target_path = os.path.join(target_folder, filename)
        resize_image(image_path, target_path, new_width, new_height)

if __name__ == "__main__":
    import sys
    """
    The script expects four arguments:
    1. The source folder containing images.
    2. The target folder to save resized images.
    3. The new width for the images.
    4. The new height for the images.
    """
    if len(sys.argv) != 5:
        print("Usage: python image_resizer_batch.py <source_folder> <target_folder> <new_width> <new_height>")
    else:
        source_folder = sys.argv[1]
        target_folder = sys.argv[2]
        new_width = int(sys.argv[3])
        new_height = int(sys.argv[4])
        batch_resize_images(source_folder, target_folder, new_width, new_height)