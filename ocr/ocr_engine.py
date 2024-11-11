import pytesseract
from PIL import Image
import logging
import yaml
import os

with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

pytesseract.pytesseract.tesseract_cmd = config.get("tesseract_path", "")
os.environ["TESSDATA_PREFIX"] = config.get("tessdata_path")

class OCREngine:
    @staticmethod
    def extract_text(image):
        try:
            return pytesseract.image_to_string(image, lang=config.get("language", "eng"))
        except Exception as e:
            logging.error(F"Error in OCR extraction: {e}")
            raise
