# Business Card Reader

A Python application for reading and extracting key information from business card images using Optical Character Recognition (OCR) with Tesseract and OpenCV. The tool processes an image of a business card and extracts information such as name, phone number, email, company name, and address.

## Features
- **OCR Extraction**: Uses Tesseract OCR to extract text from business card images.
- **Text Parsing**: Identifies and extracts key fields (name, email, phone, etc.) from raw text.

## Prerequisites

- Python 3.7+
- Tesseract OCR installed on your system ([https://github.com/tesseract-ocr/tesseract#installation](https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file#installing-tesseract))

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/business-card-reader.git
   cd business-card-reader
   ```
2. **Set up Tesseract OCR**:

   Ensure that Tesseract is installed. You may want to set the `TESSDATA_PREFIX` environment variable to the directory containing `tessdata`.

3. **Install dependencies**:

- You may want to use a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

- Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration
can be done from the `config.yaml` file, by editing the path of the tesseract executable by editing the `tesseract_path` variable, by editing the tessdata folder location through the `tessdata_path` variable and the language through the `language` variable.

## Usage
Placing the business card image in the root directory and running
```bash
python main.py
```
## Contribution
Contributions are welcome

## License
This project is licensed under the MIT license.

## Acknowledgments
- [Tesseract](https://github.com/tesseract-ocr/tesseract)
- [OpenCV](https://opencv.org)
- [ChatGpt](https://chatgpt.com/)

