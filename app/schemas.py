from pydantic import BaseModel, EmailStr, PostBase
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True  # if user doesnt provide published, it will default to true

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    created_at: datetime


class Post(PostBase):
    id: int
    created_at:datetime
    owner_id: int

    class Config:
        orm_mode = True





class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    id: int
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]
    

