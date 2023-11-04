#!/usr/bin/env python3
from PIL import Image
import sys

# Check the number of command-line arguments
if len(sys.argv) != 2:
    print ("Usage: python3 asciicode.py <IMAGE>\n   e.g., python3 asciicode.py image.png")
    sys.exit(1)

# Define the allowed image formats
allowed_formats = ["png", "jpg", "jpeg", "bmp"]

# Get the image file path from the command-line argument
img_path = sys.argv[1]

# Open the image
image = Image.open(img_path)
"""
# Check if the file format is allowed
try:
    with image as img:
        # Get the format of the image (e.g., "png", "jpeg")
        image_format = img.format
    if image_format and image_format_upper() in allowed_formats:
        print(f"Processing {image_format} image...")
    else:
        print(f"Error: Only {', '.join(allowed_formats)} image formats are allowed.")
        sys.exit(1)
except Exception as e:
    print("Error: Could not open the image file.")
    sys.exit(1)
"""
# Convert the image to grayscale
image_grayscale = image.convert("L")
print ("Break Point")

# Define the ASCII characters for conversion
ascii_chars = "@%#*+=-:. "

# Resize the image based on the number of characters you want to display per line
largeur, hauteur = image_grayscale.size
largeur_cible = 100
facteur_redimensionnement = largeur_cible / largeur
hauteur_cible = int(hauteur * facteur_redimensionnement)
image_redimensionnee = image_grayscale.resize((largeur_cible, hauteur_cible))

# Generate the ASCII image
pixels = image_redimensionnee.getdata()
ascii_image = ""
for pixel_value in pixels:
    ascii_image += ascii_chars[pixel_value // 25]

# Split the ASCII image into lines
lignes_ascii = [ascii_image[i:i+largeur_cible] for i in range(0, len(ascii_image), largeur_cible)]

# Write the ASCII image to a text file
with open("image_ascii.txt", "w") as fichier:
    for ligne in lignes_ascii:
        fichier.write(ligne + "\n")

print("The ASCII image has been saved to the image_ascii.txt file.")
