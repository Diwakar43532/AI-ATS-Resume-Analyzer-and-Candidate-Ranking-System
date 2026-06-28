import re


class RegexExtractor:

    def extract_email(self, text):

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(pattern, text)

        if match:
            return match.group()

        return None
    
    def extract_phone(self, text):

        pattern = r"(?:\+91[-\s]?)?(?:\(?0?\)?[-\s]?)?[6-9]\d{9}"

        match = re.search(pattern, text)

        if match:
            return match.group()

        return None
    
    def extract_linkedin(self, text):

        pattern = r"(?:https?://)?(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+/?"

        match = re.search(pattern, text)

        if match:
            return match.group()

        return None

    def extract_github(self, text):

        pattern = r"(?:https?://)?(?:www\.)?github\.com/[A-Za-z0-9_-]+/?"

        match = re.search(pattern, text)

        if match:
            return match.group()

        return None
    

    def extract_portfolio(self, text):

        pattern = r"https?://[^\s]+"

        matches = re.findall(pattern, text)

        for url in matches:

            if "linkedin" in url.lower():
                continue

            if "github" in url.lower():
                continue

            return url

        return None