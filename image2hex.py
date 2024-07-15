import argparse
import numpy
import sys
from PIL import Image


def is_black(pixel):
    return numpy.array_equal(pixel, [0, 0, 0])

def looks_like_black(pixel, black_threshold):
    return (
        pixel[0] < black_threshold
        and
        pixel[1] < black_threshold
        and
        pixel[2] < black_threshold
    )

def read_image_at(path):
    img = Image.open(path, "r")
    width, height = img.size
    pixel_values = list(img.getdata())
    return numpy.array(pixel_values).reshape((width, height, 3))

def convert_to_bin(image, output_path, black_threshold):
    with open(output_path, "wb") as f:
        for row in image:
            for pixel in row:
                if looks_like_black(pixel, black_threshold):
                    f.write(b"\x00")
                else:
                    f.write(b"\xFF")

def print_bin_file(file, width):
    with open(file, "rb") as f:
        i = 0
        while (byte := f.read(1)):
            print(" " if byte == b"\x00" else "X", end="")
            if i != 0 and i % width == 0:
                print("")
            i = i + 1
    print("")


parser = argparse.ArgumentParser(prog="image2hex")
parser.add_argument("--input", type=str)
parser.add_argument("--output", type=str)
parser.add_argument("--black_threshold", type=int, default=30)
args = parser.parse_args()

image = read_image_at(args.input)
width = image.shape[0]
height = image.shape[1]
print(f"image shape: {width}x{height}")

convert_to_bin(image, args.output, args.black_threshold)

print_bin_file(args.output, width)