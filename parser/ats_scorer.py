class ATSScorer:

    def calculate_score(self, result, job_description):

        score = 0

        # -------------------------
        # Resume Completeness (40)
        # -------------------------

        if result.get("name"):
            score += 4

        if result.get("email"):
            score += 4

        if result.get("phone"):
            score += 4

        if result.get("summary"):
            score += 4

        if result.get("education"):
            score += 6

        if result.get("experience"):
            score += 6

        if result.get("projects"):
            score += 4

        if result.get("certifications"):
            score += 4

        if result.get("languages"):
            score += 4

        # -------------------------
        # Skill Matching (60)
        # -------------------------

        resume_skills = [
            skill.lower()
            for skill in result.get("skills", [])
        ]

        jd_words = job_description.lower()

        matched = []
        missing = []

        for skill in resume_skills:

            if skill in jd_words:
                matched.append(skill)

        # Skills mentioned in JD
        jd_skills = []

        for word in jd_words.replace(",", " ").split():

            if word not in jd_skills:
                jd_skills.append(word)

        for skill in jd_skills:

            if skill in resume_skills:
                continue

            missing.append(skill)

        if len(resume_skills) > 0:

            score += int(
                len(matched) / len(resume_skills) * 60
            )

        score = min(score, 100)

        if score >= 90:
            recommendation = "Excellent Match"

        elif score >= 75:
            recommendation = "Strong Match"

        elif score >= 60:
            recommendation = "Average Match"

        else:
            recommendation = "Poor Match"

        return {

            "score": score,

            "matched_skills": matched,

            "missing_skills": missing,

            "matched_count": len(matched),

            "recommendation": recommendation

        }