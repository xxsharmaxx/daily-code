# Day 17: Image to Text Scanner (OCR)

from PIL import Image
import pytesseract

# Set path (Windows only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)

        print("\nExtracted Text:\n")
        print(text)

    except Exception as e:
        print("Error:", e)


# Input
image_path = input("Enter image path: ")

extract_text(image_path)
