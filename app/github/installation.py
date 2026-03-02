
from fastapi import APIRouter

router = APIRouter()

@router.get("/github/install")
def install():
    return {"status": "Redirect user to GitHub App installation URL"}
