import re

class TextCleaner:

    def clean(self, text):

        # Remove non-ASCII characters
        text = text.encode("ascii", "ignore").decode()

        # Replace bullet points
        text = text.replace("•", " ")

        # Remove extra spaces BUT keep newlines
        text = re.sub(r"[ \t]+", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n{2,}", "\n", text)

        return text.strip()


text_cleaner = TextCleaner()