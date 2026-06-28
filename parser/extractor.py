from pdfminer.high_level import extract_text
from docx import Document
import os


class TextExtractor:

    def extract(self, file_path):
        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return self.extract_pdf(file_path)

        elif extension == ".docx":
            return self.extract_docx(file_path)

        else:
            raise ValueError("Unsupported File Format")

    def extract_pdf(self, file_path):
        return extract_text(file_path)

    def extract_docx(self, file_path):
        document = Document(file_path)

        paragraphs = []

        for paragraph in document.paragraphs:
            paragraphs.append(paragraph.text)

        return "\n".join(paragraphs)

extractor = TextExtractor()
text = extractor.extract(r"D:\Python.. learnig\Resume Prediction Project\data\sample_resume\Ashish_Kumar_Resume.pdf")