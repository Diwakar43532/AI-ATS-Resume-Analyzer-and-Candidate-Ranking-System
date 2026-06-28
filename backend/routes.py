from fastapi import APIRouter
from parser.parser import ResumeParser

from fastapi import UploadFile, File

import os
import tempfile

router = APIRouter()

resume_parser = ResumeParser()


@router.get("/test")
def test():

    return {
        "message": "Routes Working"
    }

@router.post("/parse")
async def parse_resume(
    file: UploadFile = File(...)
):

    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as tmp:

        tmp.write(await file.read())
        temp_path = tmp.name

    try:

        result = resume_parser.parse_file(temp_path)

        return {
            "success": True,
            "filename": file.filename,
            "data": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)