import re


class JDMatcher:

    def match(self, resume_skills, job_description):

        # Convert JD to lowercase
        jd = job_description.lower()

        matched = []
        missing = []

        for skill in resume_skills:

            if skill.lower() in jd:
                matched.append(skill)

        # Common ATS skills
        all_skills = [
            "Python",
            "SQL",
            "Machine Learning",
            "Deep Learning",
            "Docker",
            "AWS",
            "Git",
            "GitHub",
            "FastAPI",
            "Flask",
            "Django",
            "Pandas",
            "NumPy",
            "Scikit-learn",
            "TensorFlow",
            "PyTorch",
            "Linux",
            "Kubernetes",
            "Java",
            "C++"
        ]

        for skill in all_skills:

            if skill.lower() in jd:

                if skill not in matched:
                    missing.append(skill)

        score = 0

        if len(matched) + len(missing) > 0:

            score = round(
                len(matched) /
                (len(matched) + len(missing))
                * 100
            )

        return {
            "match_score": score,
            "matched_skills": matched,
            "missing_skills": missing
        }