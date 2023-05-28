from fastapi import APIRouter, Form, HTTPException

from app.services.password_validator import is_password_valid

router = APIRouter()


@router.post("/validate-password")
def validate_password(password: str = Form(...)):
    if password is None or password.strip() == "":
        raise HTTPException(status_code=400, detail="Password must not be empty.")
    if is_password_valid(password):
        return {"valid": True}
    else:
        return {"valid": False}
