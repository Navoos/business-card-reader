import re
import logging

class TextParser:
    @staticmethod
    def parse_text(text):
        data = {
                "name": None,
                "phone": None,
                "email": None,
                "company": None,
                "address": None,
        }
        lines = text.split("\n")
        for line in lines:
            if line.strip() and "@" not in line and not re.search(r"\d", line):
                data["name"] = line.strip()
                break
        phone_pattern = r'(\+?\d[\d -]{8,}\d)'
        phones = re.findall(phone_pattern, text)
        data["phone"] = phones[0] if phones else None

        # from Wikipedia
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        emails = re.findall(email_pattern, text)
        data["email"] = emails[0] if emails else None

        for line in lines:
            if line.isupper() and not re.search(r"\d", line):
                data["company"] = line.strip()
                break
        address_pattern = r'\d+\s+\w+\s+\w+'
        for line in lines:
            if re.search(address_pattern, line):
                data["address"] = line.strip()
                break

        return data

