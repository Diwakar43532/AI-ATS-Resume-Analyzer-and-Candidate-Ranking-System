from pydantic import BaseModel


class ParseResponse(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    linkedin: str | None = None
    github: str | None = None
    ats_score: int | None = None
    matched_skills: list = []