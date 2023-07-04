from fastapi import FastAPI
from app import models
from app.routers import users, auth, passengers
from app.database import engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(passengers.router)
