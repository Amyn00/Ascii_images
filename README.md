# Image to ASCII Converter
<img src="https://github.com/Amyn00/Ascii_images/blob/main/image/test.png" width="1000px" height="500px"/>

This Python script converts images to ASCII art, providing a text-based representation of the image.
## Requirements
* Pyhton 3 
	* (check if Python 3 exist)
	```bash
	python3 --version
	```
* Pillow library (PIL)
You can install the pillow library using pip:
```bash
pip install Pillow
```
## Usage
1. Clone this repository or download the Python script (asciicode.py) to your local machine.
```bash
git clone https://github.com/Amyn00/Ascii_images.git
```
2. Navigate to the directory
```bash
cd Ascii_image
```

3. Prepare an image in one of the allowed formats (PNG, JPG, JPEG, BMP) that you want to convert to ASCII art. Save the image in the same directory as the Python script or provide the full path to the image in the command-line arguments.

4. Run the script with the image file as an argument. For example:
```bash
python3 asciicode.py image.png
```
or
```bash
./asciicode.py image.png
```
Replace image.png with the actual name of your image file.

5. The script will check if the image format is allowed, and if it is, it will process the image to generate an ASCII representation. The resulting ASCII art will be saved to a file named **`image_ascii.txt`** in the same directory.

6. Open and view the **`image_ascii.txt`** file to see the ASCII representation of the image.

## Supported Image Formats

* PNG
* JPG (JPEG)
* BMP

## Customization
You can customize the script to change the output image size, the characters used for the conversion, or other settings according to your preferences.

## Author
**Mohammed Amine Mounjid**
