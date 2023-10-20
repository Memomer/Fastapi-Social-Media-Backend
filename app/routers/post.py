
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import schemas, models, utils
from typing import Optional, List
from ..database import get_db
from sqlalchemy.orm import Session
from .. import oauth2

router = APIRouter(
    prefix = "/posts",
    tags = ["Posts"]   
)

@router.get("/", response_model = List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    #cursor.execute("""SELECT * FROM table_1""")
    #posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return {"data":posts}       #the first path operation that matches is the first one that runs

                                            #path operation forms a list
@router.post("/", status_code=status.HTTP_201_CREATED, response_model = schemas.Post)
def create_posts(post: schemas.Post, db: Session = Depends(get_db),  get_current_user: int = Depends(oauth2.get_current_user)): 
    # cursor.execute("""INSERT INTO table_1 (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))     #post will get the data from frontend with schema intact #schema is rules for send payload to server #automatic validation
    # new_post = cursor.fetchone()
    # conn.commit()
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post}
    

@router.get("/{id}", response_model=schemas.Post)
def get_post(id : int, db: Session = Depends(get_db)):

    # cursor.execute(f""" SELECT * FROM table_1 WHERE id= %s""", (str(id),))
    # selected_post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} was not found")
    
    return {"data": post}


@router.delete("/{id}", response_model=schemas.Post)
def delete_post(id:int, db : Session = Depends(get_db), status_code = status.HTTP_204_NO_CONTENT):
    # cursor.execute("""DELETE FROM table_1 WHERE id = %s returning *""", (str(id),))
    # deleted_post =  cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} doesn't exist")
    db.delete(post)
    db.commit()
    
    return {'message':post}

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, ):
    #cursor.execute("""UPDATE table_1 SET title = %s, content = %s, published = %s where id= %s RETURNING *""", (post.title, post.content, post.published, (str(id))))
    
    #updated_post = cursor.fetchone()
    #conn.commit()

    if post == None:
        raise HTTPException(status_code= status.HTTP_204_NO_CONTENT);
    
    return {"data":updated_post}
