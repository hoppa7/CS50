import sys
from PIL import Image, ImageOps
import os

command_line_length = len(sys.argv)

if not command_line_length == 3:
    if command_line_length > 3:
        sys.exit("Too many command-line arguments")
    elif command_line_length < 3:
        sys.exit("Too few command-line arguments")

input_one = os.path.splitext(sys.argv[1])
input_two = os.path.splitext(sys.argv[2])

if not input_one[1].lower() in [".jpeg", ".jpg", ".png"] or not input_two[1].lower() in [".jpeg", ".jpg", ".png"]:
    sys.exit("Invalid Format")

if input_one[1] != input_two[1]:
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    input_img = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File not found.")

size = shirt.size
input_img = ImageOps.fit(input_img, size)
input_img.paste(shirt, shirt)
input_img.save(sys.argv[2])
