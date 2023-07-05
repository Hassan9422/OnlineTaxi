from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, Response
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


@router.get("/", response_model=List[schemas.UserResponse])
def get_all_users(db: session = Depends(database.get_db), current_user: int = Depends(oauth2.verify_access_token)):
    users = db.query(models.User).all()

    if not users:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="There is no passengers!")

    return users


@router.put("/{id}", response_model=schemas.UserResponse)
def update_one_user(id: int, user: schemas.UserCreate, db: session = Depends(database.get_db),
                    current_user: int = Depends(oauth2.verify_access_token)):
    found_user = db.query(models.User).filter(models.User.id == id)

    if not found_user.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"user with id={id} does not exist!")

    if not found_user.first().id == current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="You can not update another user other than yourself!")
    user.password = utils.password_hash(user.password)
    print(user)
    found_user.update(user.dict(), synchronize_session=False)
    db.commit()

    return found_user.first()


@router.delete("/{id}")
def delete_one_user(id: int, db: session = Depends(database.get_db),
                    current_user: int = Depends(oauth2.verify_access_token)):
    found_user = db.query(models.User).filter(models.User.id == id)

    if not found_user.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"user with id={id} does not exist!")

    if not found_user.first().id == current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="You can not update another user other than yourself!")

    found_user.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
