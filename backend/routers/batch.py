from fastapi import APIRouter, UploadFile, File, Form
import tempfile
import shutil
import os
from typing import List

from parser.parser import ResumeParser
from parser.ats_scorer import ATSScorer

router = APIRouter(
    prefix="/batch",
    tags=["Batch Ranking"]
)

parser = ResumeParser()
scorer = ATSScorer()

@router.post("/parse")
async def batch_parse(
    files: list[UploadFile] = File(...),
    job_description: str = Form(...)
):
    results = []

    for file in files:

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

            results.append({
            "filename": file.filename,
            "data": result
            })

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    results.sort(
    key=lambda x: x["data"]["ats_score"],
    reverse=True
   )
    for rank, resume in enumerate(results, start=1):
        resume["rank"] = rank

    return {
    "success": True,
    "total_resumes": len(results),
    "results": results
}