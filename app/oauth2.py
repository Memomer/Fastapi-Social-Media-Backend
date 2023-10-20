from jose import JWTError, jwt
from datetime import datetime, timedelta
import schemas
from fastapi import status, HTTPEXception, Depends
from fastapi.security import OAuth2PasswordBearer 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY ="2ef36d0cc998578e2d1fd1d02824878d2aabcb31ef33046644f3613a5a6d2d01"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() +timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    id: str = payload.get("user_id")
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=[ALGORITHM])

    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    id: str = payload.get("user_id")

    if id is None:
        raise credentials_exception
    
    token_data = schemas.TokenData(id=id)


  except JWTError:
     raise credentials_exception
  
  return token_data

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
   credentials_exception = HTTPEXception(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"could not validate credentials", headers = {"WWW=Authenticate":"Bearer"}) 