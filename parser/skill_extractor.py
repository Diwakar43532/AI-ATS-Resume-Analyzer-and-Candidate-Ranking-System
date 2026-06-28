# import json

# class SkillExtractor:

#     def __init__(self):

#         with open(r"data\skills.json") as f:
#             self.skills = json.load(f)

#     def extract_skills(self, text):

#         found = []

#         text = text.lower()

#         for skill in self.skills:

#             if skill.lower() in text:
#                 found.append(skill)

#         return list(set(found))

import json
import re
from pathlib import Path


class SkillExtractor:

    def __init__(self):

        # Project root folder
        BASE_DIR = Path(__file__).resolve().parent.parent

        # Full path to skills.json
        skill_file = BASE_DIR / "data" / "skills.json"

        

        with open(skill_file, "r", encoding="utf-8") as f:
            self.skills = json.load(f)

    def extract_skills(self, text):

        text = text.lower()

        found = []

        

        for skill in self.skills:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, text):
                
                found.append(skill)
        return sorted(list(set(found)))
