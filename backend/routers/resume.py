import os
import shutil
import tempfile

from fastapi import APIRouter, UploadFile, File, Form

from parser.parser import ResumeParser
from parser.ats_scorer import ATSScorer

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

parser = ResumeParser()
scorer = ATSScorer()


@router.post("/parse")
async def parse_resume(
    file: UploadFile = File(...),
    job_description: str = Form("")
):

    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:

        shutil.copyfileobj(file.file, tmp)
        temp_path = tmp.name

    result = parser.parse_file(temp_path)

    ats = scorer.calculate_score(
        result,
        job_description
    )

    result["ats_score"] = ats["score"]
    result["matched_skills"] = ats["matched_skills"]
    result["matched_count"] = ats["matched_count"]

    os.remove(temp_path)

    return result

@router.post("/match")
async def match_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as tmp:

        shutil.copyfileobj(file.file, tmp)
        temp_path = tmp.name

    try:
        result = parser.parse_file(temp_path)

        ats = scorer.calculate_score(
            result,
            job_description
        )

        result["ats_score"] = ats["score"]
        result["matched_skills"] = ats["matched_skills"]
        result["matched_count"] = ats["matched_count"]

        return result

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)