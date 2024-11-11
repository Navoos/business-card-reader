import logging
from ocr.image_preprocessor import ImagePreProcessor
from ocr.ocr_engine import OCREngine
from parser.text_parser import TextParser

logging.basicConfig(level=logging.DEBUG)

def process_business_card(image_path):
    try:
        processed_image = ImagePreProcessor.preprocess_image(image_path)

        raw_txt = OCREngine.extract_text(processed_image)
        logging.info(f"Extracted Text: {raw_txt}")

        parsed_data = TextParser.parse_text(raw_txt)
        logging.info(f"Parsed Data: {parsed_data}")
        
        return parsed_data
    except Exception as e:
        logging.error(f"Error in processing business card: {e}")
        return None

if __name__ == "__main__":
    image_path = "business_card.jpeg"
    result = process_business_card(image_path)
    # print(result)
