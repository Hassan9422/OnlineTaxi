from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import session
from app import schemas, database, models, utils, oauth2

router = APIRouter(prefix="/login", tags=["Login User"])


@router.post("/")
def login_suer(user: schemas.UserLogin, db: session = Depends(database.get_db)):

    found_user = db.query(models.User).filter(models.User.phone_number == user.phone_number).first()

    if not found_user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="user not found!")

    if not utils.verify_password(user.password, found_user.password):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="password wrong!")

    token = oauth2.create_access_token(data={"id": found_user.id, "name": found_user.name})

    return {"token": token, "token_type": "Bearer"}

