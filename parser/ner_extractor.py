import spacy

class NERExtractor:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_name(self, text):
        lines = text.split("\n")
        for line in lines:
            line = line.strip()
            if not line:
                continue
       # Skip non-name lines
            if "@" in line:
                continue

            if "linkedin" in line.lower():
                continue

            if "github" in line.lower():
                continue

            if "|" in line:
                continue

            # First valid line is the name
            return line.upper()

        return None
    
    
    def extract_entities(self, text):

        doc = self.nlp(text)

        entities = []

        for ent in doc.ents:
            entities.append(
                {
                    "text": ent.text,
                    "label": ent.label_
                }
            )

        return entities