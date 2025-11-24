from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from blog import models, schemas
from blog.hashing import Hash


def create_user(db: Session,request: schemas.User):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id, db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user