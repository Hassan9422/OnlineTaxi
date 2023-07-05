from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import session

from app import schemas, models, database, utils
from app import oauth2
router = APIRouter(prefix="/passengers", tags=['Passenger'])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponsePassenger)
def create_one_passenger(passenger: schemas.CreatePassenger, db: session = Depends(database.get_db), current_user: int = Depends(oauth2.verify_access_token)):

    new_passenger = models.Passenger(user_id=current_user.id, **passenger.dict())
    print(new_passenger)
    db.add(new_passenger)
    db.commit()
    db.refresh(new_passenger)
    print(new_passenger)
    return new_passenger


@router.get('/{id}', response_model=schemas.ResponsePassenger)
def get_one_passenger(id: int, db: session = Depends(database.get_db)):
    passenger = db.query(models.Passenger).filter(models.Passenger.passenger_id == id).first()
    if not passenger:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"the user with id={id} does not exist!")
    print(passenger)
    print(type(passenger))

    return passenger


@router.get("/", response_model=List[schemas.ResponsePassenger])
def get_all_passengers(db: session = Depends(database.get_db), current_user: int = Depends(oauth2.verify_access_token)):
    passengers = db.query(models.Passenger).all()

    if not passengers:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="There is no passengers!")

    return passengers


@router.put("/{id}", response_model=schemas.ResponsePassenger)
def update_one_passenger(id: int, passenger: schemas.CreatePassenger, db: session = Depends(database.get_db),
                         current_user: int = Depends(oauth2.verify_access_token)):
    found_passenger = db.query(models.Passenger).filter(models.Passenger.passenger_id == id)

    if not found_passenger.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"passenger with id={id} does not exist!")

    if not found_passenger.first().user_id == current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="You can not update another passenger other than yourself!")

    found_passenger.update(passenger.dict(), synchronize_session=False)
    db.commit()

    return found_passenger.first()


@router.delete("/{id}")
def delete_one_passenger(id: int, db: session = Depends(database.get_db),
                         current_user: int = Depends(oauth2.verify_access_token)):
    found_passenger = db.query(models.Passenger).filter(models.Passenger.passenger_id == id)

    if not found_passenger.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"passenger with id={id} does not exist!")

    if not found_passenger.first().user_id == current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="You can not delete another passenger other than yourself!")

    found_passenger.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
