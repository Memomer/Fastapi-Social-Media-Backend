from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel, BaseSettings
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
import schemas
import utils
from .routers import post, user, auth
from .config import Settings


models.Base.metadata.create_all(bind=engine)



app = FastAPI()





settings = Settings()

        
    #error catching and while loop so the fastapi server doesn't work unless we successfully get a connection
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='postgres', user='user_1', password='mayank', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database Connection was succesfull!")
        break
    except Exception as error:
        print("connecting to database failed")
        print("error:", error)
        time.sleep(2)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")                                  #path operation 
def root():                                    #async?  #name of the function can be anything
    return {"message":"Hello World"}           #data that is sent back to user 

@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    print(posts)
    return {"status":posts}


