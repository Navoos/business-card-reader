import cv2
import logging

class ImagePreProcessor:
    @staticmethod
    def preprocess_image(image_path):
        try:
            # read image
            image = cv2.imread(image_path)
            # convert to gray scale for better readability
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # reduce noise
            gray = cv2.bilateralFilter(gray, 11, 17, 17)
            return gray
        except Exception as e:
            logging.error(f"Error in image preprocessing: {e}")
            raise
