from typing import Optional
from pydantic import BaseModel, EmailStr, validator


class UserBase(BaseModel):
    name: str
    email: Optional[EmailStr] = None


class UserCreate(UserBase):
    address: str
    phone_number: int
    password: str

    @validator('phone_number')
    def check_phone_number(cls, value):
        if len(str(value)) < 10:
            raise ValueError("the number has to have al least 10  digits!!")
        if value < 0:
            raise ValueError("enter a correct number!!")
        return value


class UserResponse(UserBase):
    id: int
    phone_number: int

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    id: int
    name: str


class UserLogin(BaseModel):
    phone_number: int
    password: str


class CreatePassenger(BaseModel):
    source: str
    destination: str


class UserInfo(BaseModel):
    name: str
    phone_number: int

    class Config:
        orm_mode = True


class ResponsePassenger(BaseModel):
    passenger_id: int
    source: str
    destination: str
    user_info: UserInfo

    class Config:
        orm_mode = True
