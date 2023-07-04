from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import session

from app import schemas, models, database, utils, oauth2

router = APIRouter(prefix="/users", tags=['Users'])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_one_user(user: schemas.UserCreate, db: session = Depends(database.get_db)):
    user.password = utils.password_hash(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/{id}', response_model=schemas.UserResponse)
def get_one_user(id: int, db: session = Depends(database.get_db), curent_user: int = Depends(oauth2.verify_access_token)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"the user with id={id} does not exist!")
    print(user)
    print(type(user))

    return user
