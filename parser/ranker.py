class ResumeRanker:

    def rank(self, resumes):

        for resume in resumes:

            ats = resume.get("ats_score", 0)

            jd = resume.get("job_match", {}).get("match_score", 0)

            # Weighted Score
            resume["final_score"] = round(
                ats * 0.6 + jd * 0.4,
                2
            )

        resumes.sort(
            key=lambda x: x["final_score"],
            reverse=True
        )

        return resumes