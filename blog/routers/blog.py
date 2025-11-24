from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from blog import models
from blog.database import get_db
from blog.repository import blog
from blog.schemas import ShowBlog, Blog, User
from blog.oauth2 import get_current_user

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


@router.get('/', response_model=List[ShowBlog], status_code=status.HTTP_200_OK)
def all_blogs(db: Session = Depends(get_db),
              get_current_user: User = Depends(get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: Blog, db: Session = Depends(get_db),
                get_current_user: User = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.email == get_current_user.email).first()
    return blog.create_blog(db, request,user)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(get_db),
                   get_current_user: User = Depends(get_current_user)):
    return blog.get_blog(db, id)


@router.delete('/{id}')
def delete_blog_by_id(id: int, db: Session = Depends(get_db)
                      , get_current_user: User = Depends(get_current_user)):
    return blog.delete_blog(db, id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: Blog, db: Session = Depends(get_db),
                get_current_user: User = Depends(get_current_user)):
    return blog.update_blog(db, request, id)
