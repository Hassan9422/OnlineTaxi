from fastapi import APIRouter, Depends, status, HTTPException
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
    passenger = db.query(models.Passenger).filter(models.Passenger.id == id).first()
    if not passenger:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"the user with id={id} does not exist!")
    print(passenger)
    print(type(passenger))

    return passenger
