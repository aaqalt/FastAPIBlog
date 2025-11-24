
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from blog import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(db: Session, request: schemas.Blog,user):
    new_blog = models.Blog(title=request.title, content=request.content,creator_id=user.id)
    db.add(new_blog)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted successfully"}

def update_blog(db: Session, request: schemas.Blog,id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return {"message": "Blog updated successfully"}

def get_blog(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return blog