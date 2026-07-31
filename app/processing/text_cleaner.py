import re

class TextCleaner:
    @staticmethod
    def clean(text:str)-> str:
        """
        Basic text normalization
        """
        text = re.sub(r"\n+","\n",text)
        text = re.sub(r"[\t]+"," ", text)
        text = text.strip()

        return text