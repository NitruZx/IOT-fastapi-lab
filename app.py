from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import models
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
router_v1 = APIRouter(prefix='/api/v1')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils

@router_v1.get('/books')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router_v1.get('/books/{book_id}')
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

@router_v1.post('/books')
async def create_book(book: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newbook = models.Book(title=book['title'], 
                          author=book['author'], 
                          year=book['year'], 
                          is_published=book['is_published'],
                          description=book['description'],
                          synopsis=book['synopsis'],
                          image_url=book['image_url'])
    db.add(newbook)
    db.commit()
    db.refresh(newbook)
    response.status_code = 201
    return newbook

@router_v1.patch('/books/{book_id}')
async def update_book(book_id: str, book: dict, response: Response, db: Session = Depends(get_db)):
    bk = db.query(models.Book).filter(models.Book.id == book_id).first()
    if (bk is None):
        response.status_code = 400
        return {
            "message" : "Book's ID not found."
        }
    for key in book:
        setattr(bk, key, book[key])
    db.commit()
    response.status_code = 201
    return {
        "message" : "Book's info edited successfully"
    }

@router_v1.delete('/books/{book_id}')
async def delete_book(book_id: str, response: Response, db: Session = Depends(get_db)):
    bk = db.query(models.Book).filter(models.Book.id == book_id).first()
    if (bk is not None):
        db.delete(bk)
        db.commit()
        response.status_code = 201
        return {
            "message" : "delete info successfully"
        }
    response.status_code = 400
    return {
        "message" : "Book's ID not found."
    }

@router_v1.get('/students')
async def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@router_v1.get('/students/{student_id}')
async def get_student(student_id: str, db: Session = Depends(get_db)):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

@router_v1.post('/students')
async def add_student(student: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newstu = models.Student(id=student['id'], firstname=student['firstname'], lastname=student['lastname'], dob=student['dob'], sex=student['sex'])
    db.add(newstu)
    db.commit()
    db.refresh(newstu)
    response.status_code = 201
    return newstu

@router_v1.patch('/students/{student_id}')
async def update_student(student_id: str, student: dict, response: Response, db: Session = Depends(get_db)):
    stu = db.query(models.Student).filter(models.Student.id == student_id).first()
    if (stu is None):
        response.status_code = 400
        return {
            "message" : "Student's ID not found."
        }
    keys = ["id", "firstname", "lastname", "dob", "sex"]
    for key in keys:
        if key in student:
            setattr(stu, key, student[key])
    db.commit()
    response.status_code = 201
    return {
        "message" : "Student's info edited successfully"
    }

@router_v1.delete('/students/{student_id}')
async def delete_student(student_id: str, response: Response, db: Session = Depends(get_db)):
    stu = db.query(models.Student).filter(models.Student.id == student_id).first()
    if (stu is not None):
        db.delete(stu)
        db.commit()
        response.status_code = 201
        return {
            "message" : "delete info successfully"
        }
    response.status_code = 400
    return {
        "message" : "Student's ID not found."
    }
    
@router_v1.get('/menus')
async def get_menus(db: Session = Depends(get_db)):
    return db.query(models.Menu).all()

@router_v1.get('/menus/{menu_id}')
async def get_menu(menu_id: int, db: Session = Depends(get_db)):
    return db.query(models.Menu).filter(models.Menu.menu_id == menu_id).first()

@router_v1.post('/menus')
async def create_menu(menu: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newmenu = models.Menu(menu_name=menu['menu_name'], 
                          menu_description=menu['menu_description'],
                          menu_price=menu['menu_price'],
                          menu_image=menu['menu_image'])
    db.add(newmenu)
    db.commit()
    db.refresh(newmenu)
    response.status_code = 201
    return newmenu

@router_v1.patch('/menus/{menu_id}')
async def update_menu(menu_id: str, menu: dict, response: Response, db: Session = Depends(get_db)):
    mn = db.query(models.Menu).filter(models.Menu.menu_id == menu_id).first()
    if (mn is None):
        response.status_code = 400
        return {
            "message" : "Menu's ID not found."
        }
    for key in menu:
        setattr(mn, key, menu[key])
    db.commit()
    response.status_code = 201
    return {
        "message" : "Menu's info edited successfully"
    }

@router_v1.delete('/menus/{menu_id}')
async def delete_menu(menu_id: str, response: Response, db: Session = Depends(get_db)):
    mn = db.query(models.Menu).filter(models.Menu.menu_id == menu_id).first()
    if (mn is not None):
        db.delete(mn)
        db.commit()
        response.status_code = 201
        return {
            "message" : "delete menu's info successfully"
        }
    response.status_code = 400
    return {
        "message" : "Menu's ID not found."
    }

app.include_router(router_v1)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
