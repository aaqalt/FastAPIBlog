from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from blog.database import get_db
from blog.repository import user
from blog.schemas import ShowUser, User

router = APIRouter(
    tags=['users'],
    prefix='/user',
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create_user(db, request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return user.get_user(id,db)
