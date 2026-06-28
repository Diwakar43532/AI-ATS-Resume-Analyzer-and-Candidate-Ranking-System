class ResumeValidator:

    def validate(self, result):

        warnings = []

        if not result.get("email"):
            warnings.append("Email not found")

        if not result.get("phone"):
            warnings.append("Phone number not found")

        if not result.get("linkedin"):
            warnings.append("LinkedIn profile missing")

        if not result.get("github"):
            warnings.append("GitHub profile missing")

        if not result.get("skills"):
            warnings.append("No skills detected")

        if not result.get("education"):
            warnings.append("Education details missing")

        if not result.get("experience"):
            warnings.append("Experience details missing")

        if not result.get("projects"):
            warnings.append("Projects not found")

        return warnings