

class SectionParser:

    SECTION_HEADERS = {
        "education": ["education", "educational qualification", "academic qualification","qalification"],
        "experience": ["experience", "work experience", "internship experience", "professional experience", "work history", "employment history"],
        "skills": ["skills", "technical skills", "technical expertise","core skills"],
        "projects": ["projects", "projects & research", "research","academic projects"],
        "summary": ["summary", "career objective", "objective", "profile","professional summary"],
        "certifications": ["certifications", "certificates"],
        "achievements": ["achievements", "awards", "honors"],
        "languages": ["languages", "language proficiency", "language skills"]
    }

    def split_sections(self, text):
        sections = {
        "header": [],
        "summary": [],
        "skills": [],
        "education": [],
        "projects": [],
        "experience": [],
        "certifications": [],
        "achievements": [],
        "languages": []
        }
        current_section = "header"
        lines = text.split("\n")
        for line in lines:
            line = line.strip()

            if not line:
                continue

            lower = line.lower().strip()

           # Remove ":" at the end of headings
            lower = lower.rstrip(":")

            heading_found = False

            for section, keywords in self.SECTION_HEADERS.items():

                for keyword in keywords:

                    if lower == keyword:

                        current_section = section

                        heading_found = True

                        break

                if heading_found:
                    break

            if not heading_found:
                sections[current_section].append(line)

        return sections