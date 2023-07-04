from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import session
from app import schemas, database, models
from app.config import setting
from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

ALGORITHM = setting.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = setting.access_token_expire_minutes
SECRET_KEY = setting.secret_key


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    access_token = jwt.encode(claims=to_encode, algorithm=ALGORITHM, key=SECRET_KEY)
    return access_token


def verify_access_token(token: str = Depends(oauth2_scheme), db: session = Depends(database.get_db)):
    print("11111111111111")
    credentials_error = HTTPException(status.HTTP_403_FORBIDDEN, detail="You are not authorized to do this action!")
    try:
        payload_data = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        id, name = payload_data.get('id'), payload_data.get('name')
        print("2222222222222")

        # first, we have to check whether these fields exist or not
        if not id or not name:
            raise credentials_error
        # then we have to check they are in a correct format according to the schema. "token_payload" is an object of the ""TokenData" class
        print("333333333333")

        token_payload = schemas.TokenData(id=id, name=name)
        print("444444444444")

    except JWTError:
        raise credentials_error

    # getting the user
    user = db.query(models.User).filter(models.User.id == token_payload.id, models.User.name == token_payload.name).first()
    print("5555555555555")

    if not user:
        raise credentials_error
    print("66666666666")

    return user
