from PIL import Image
import pytesseract
import requests
from io import BytesIO

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# List of all image URLs extracted from the HTML
image_urls = [
    "https://storage.googleapis.com/swayam-node1-production.appspot.com/assets/img/noc19_mg54/a7q1.PNG",
    "https://storage.googleapis.com/swayam-node1-production.appspot.com/assets/img/noc19_mg54/a7q2.PNG",
    "https://storage.googleapis.com/swayam-node1-production.appspot.com/assets/img/noc19_mg54/a7q3.PNG",
    "https://storage.googleapis.com/swayam-node1-production.appspot.com/assets/img/noc19_mg54/a7q4.PNG",
    "https://storage.googleapis.com/swayam-node1-production.appspot.com/assets/img/noc19_mg54/a7q5.PNG",
    "https://storage.googleapis.com/swayam-node1-production.appspot.com/assets/img/noc19_mg54/a7q6.PNG",
    "https://storage.googleapis.com/swayam-node1-production.appspot.com/assets/img/noc19_mg54/a7q7.PNG",
    "https://storage.googleapis.com/swayam-node1-production.appspot.com/assets/img/noc19_mg54/a7q8.PNG",
    "https://storage.googleapis.com/swayam-node1-production.appspot.com/assets/img/noc19_mg54/a7q9.PNG",
    "https://storage.googleapis.com/swayam-node1-production.appspot.com/assets/img/noc19_mg54/a7q10.PNG"
]

# File to save all questions
output_file = "all_questions.txt"

# Open the file in write mode
with open(output_file, "w", encoding="utf-8") as file:
    for idx, url in enumerate(image_urls):
        try:
            # Download the image
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            img = Image.open(BytesIO(response.content))

            # Extract text using OCR
            text = pytesseract.image_to_string(img)

            # Write the question text to the file with numbering
            file.write(f"Question {idx + 1}:\n{text}\n\n")
            print(f"Extracted text from {url} and saved to {output_file}")
        except Exception as e:
            print(f"Failed to process {url}: {e}")

print(f"All questions have been saved to {output_file}.")
