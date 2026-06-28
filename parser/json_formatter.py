import re


class JSONFormatter:

    DEGREES = [
        "B.Tech",
        "B.E",
        "BCA",
        "B.Sc",
        "MCA",
        "M.Tech",
        "M.Sc",
        "MBA",
        "Diploma",
        "Bachelor",
        "Master",
        "Class XII",
        "Class X",
        "Intermediate",
        "High School"
    ]

    # ==========================
    # EDUCATION FORMATTER
    # ==========================

    def format_education(self, education_lines):

        
        result = []

        for line in education_lines:

            line = line.strip()

            if not line:
                continue

            education = {
                "degree": "",
                "college": "",
                "year": "",
                "cgpa": "",
                "percentage": ""
            }

            # -------------------------
            # Degree
            # -------------------------
            for degree in self.DEGREES:

                if degree.lower() in line.lower():
                    education["degree"] = degree
                    break

            # If degree not found, use first part
            if not education["degree"]:

                if "," in line:
                    education["degree"] = line.split(",")[0].strip()
                else:
                    education["degree"] = line

            # -------------------------
            # College
            # -------------------------
            if "," in line:

                parts = line.split(",")

                if len(parts) > 1:
                    education["college"] = parts[1].split("(")[0].strip()

            # -------------------------
            # Year
            # -------------------------
            year = re.search(r"(20\d{2}(?:-20\d{2})?)", line)

            if year:
                education["year"] = year.group(1)

            # -------------------------
            # CGPA
            # -------------------------
            cgpa = re.search(
                r"CGPA[: ]*([\d.]+)(?:/10)?",
                line,
                re.IGNORECASE
            )

            if cgpa:
                education["cgpa"] = cgpa.group(1)

            # -------------------------
            # Percentage
            # -------------------------
            percentage = re.search(
                r"(\d+(?:\.\d+)?)\s*%",
                line
            )

            if percentage:
                education["percentage"] = percentage.group(1)

            result.append(education)

        return result

    # ==========================
    # EXPERIENCE FORMATTER
    # ==========================

    def format_experience(self, experience_lines):

        if not experience_lines:
            return []

        experience = {
            "role": "",
            "company": "",
            "duration": "",
            "description": []
        }

        first = experience_lines[0]

        # Format:
        # Role | Company

        if "|" in first:

            parts = first.split("|")

            experience["role"] = parts[0].strip()
            experience["company"] = parts[1].strip()

        # Format:
        # Intern at ABC Technologies (3 months)

        elif " at " in first.lower():

            parts = re.split(r"\bat\b", first, flags=re.IGNORECASE)

            experience["role"] = parts[0].strip()

            company = parts[1].strip()

            if "(" in company:

                experience["company"] = company.split("(")[0].strip()

                experience["duration"] = (
                    company.split("(")[1]
                    .replace(")", "")
                    .strip()
                )

            else:

                experience["company"] = company

        # Second line may contain duration

        if len(experience_lines) > 1:

            if not experience["duration"]:

                experience["duration"] = experience_lines[1]

        # Remaining lines are descriptions

        for line in experience_lines[2:]:

            line = line.replace("-", "").strip()

            if line:
                experience["description"].append(line)

        return [experience]

    # ==========================
    # PROJECT FORMATTER
    # ==========================

    def format_projects(self, project_lines):

        projects = []

        current_project = None

        for line in project_lines:

            line = line.strip()

            if not line:
                continue

            # Remove numbering

            if re.match(r"^\d+\.", line):

                line = re.sub(r"^\d+\.\s*", "", line)

            # Remove bullets

            if line.startswith("-") or line.startswith("•"):

                line = line[1:].strip()

            # Description

            if current_project and (
                line.lower().startswith("develop")
                or line.lower().startswith("built")
                or line.lower().startswith("using")
                or line.lower().startswith("extract")
                or line.lower().startswith("logistic")
                or line.lower().startswith("random")
            ):

                current_project["description"] += " " + line

            else:

                current_project = {
                    "title": line,
                    "description": ""
                }

                projects.append(current_project)

        return projects