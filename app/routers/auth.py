from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import schemas
from .. import database, models, oauth2
import utils
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
 
    if not user:
        raise HTTPException(status_code = status.HTTP_404_FORBIDDEN, detail = f"invalid credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail = f'invalid token')

    access_token = oauth2.create_acess_token(data = {"user_id": user.id}) 


    return {"acess-token":access_token, "tokentype": "bearer"}