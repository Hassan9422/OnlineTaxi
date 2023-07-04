from sqlalchemy import Integer, Column, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True, server_default=None)
    address = Column(String, nullable=False)
    phone_number = Column(BigInteger, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Passenger(Base):
    __tablename__ = "passengers"

    passenger_id = Column(Integer, primary_key=True, nullable=False)
    source = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    user_info = relationship("User")
