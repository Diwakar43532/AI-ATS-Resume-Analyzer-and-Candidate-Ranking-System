from parser.json_formatter import JSONFormatter
from parser.extractor import TextExtractor
from parser.cleaner import TextCleaner
from parser.regex_extractor import RegexExtractor
from parser.section_parser import SectionParser
from parser.ner_extractor import NERExtractor
from parser.skill_extractor import SkillExtractor
from parser.ats_scorer import ATSScorer
from parser.validator import ResumeValidator
from parser.exporter import Exporter
from parser.jd_matcher import JDMatcher


class ResumeParser:

    def __init__(self):
        self.extractor = TextExtractor()
        self.cleaner = TextCleaner()
        self.regex = RegexExtractor()
        self.section = SectionParser()
        self.ner = NERExtractor()
        self.skill = SkillExtractor()
        self.formatter = JSONFormatter()
        self.scorer = ATSScorer()
        self.validator = ResumeValidator()
        self.exporter = Exporter()
        self.jd_matcher = JDMatcher()

    
    def parse_file(self, file_path):

        # Step 1: Extract text
        text = self.extractor.extract(file_path)

        # Step 2: Clean text
        clean_text = self.cleaner.clean(text)

        
        
        

        # Step 3: Split into sections
        sections = self.section.split_sections(clean_text)
        
        print(sections)
        
        

        # Step 4: Build result
        result = {
            "name": self.ner.extract_name(clean_text),
            "email": self.regex.extract_email(clean_text),
            "phone": self.regex.extract_phone(clean_text),
            "linkedin": self.regex.extract_linkedin(clean_text),
            "github": self.regex.extract_github(clean_text),
            "skills": self.skill.extract_skills(clean_text),
            "summary": sections.get("summary", []),
            "portfolio": self.regex.extract_portfolio(clean_text),
            "education": self.formatter.format_education(
                sections.get("education", [])
           ),
           "experience": self.formatter.format_experience(
               sections.get("experience", [])
            ),
            "projects": self.formatter.format_projects(
                sections.get("projects", [])
            ),
            
            "certifications": sections.get("certifications", []),

            "languages": sections.get("languages", [])

        }
        
        # ATS score is calculated separately in the UI
        result["warnings"] = self.validator.validate(result)

        self.exporter.export_json(result)

        self.exporter.export_csv(result)

        
        return result