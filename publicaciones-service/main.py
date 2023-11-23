import os 
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, Form, status
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List
from pydantic import BaseModel
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import httpx



app = FastAPI()
client = httpx.AsyncClient()

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)



app.mount("/static", StaticFiles(directory="static"), name="static")

# Redirect root to index.html
@app.get("/templates/opciones-page")
async def read_root():
    return RedirectResponse(url="/opciones.html")


# Modelo de datos para la publicación
class Post(Base):
    __tablename__ = 'posts'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    content = Column(String(500))
    date = Column(DateTime)
    post_type = Column(String(30))

# Crear la tabla si no existe
Base.metadata.create_all(bind=engine)

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

# Modelo Pydantic para la creación de publicaciones
class PostCreate(BaseModel):
    username: str
    content: str
    date: datetime
    post_type: str

class PostResponse(BaseModel):
    id: int
    username: str
    content: str
    date: datetime
    post_type: str

@app.post("/auth/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserRegister):
    response = client.post(f"{AUTH_SERVICE_URL}/register", json=user.dict())
    if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
        try:
            return response.json()
        except ValueError:
            # decide how to handle a server that's misbehaving to this extent
            return {"message": response.text}
    return {"message": response.text}

@app.post("/auth/login")
async def login_user(user: UserLogin):
    response = client.post(f"{AUTH_SERVICE_URL}/login", json=user.dict())
    if (response.status_code != 400 and response.headers["content-type"].strip().startswith("application/json")):
        try:
            return response.json()
        except ValueError:
            # decide how to handle a server that's misbehaving to this extent
            return {"message": response.text}
    return {"message": response.text}
    


#@app.get("/create-post", response_class=HTMLResponse)
#async def create_post(request: Request):
#    return templates.TemplateResponse("create_post.html", {"request": request})

#@app.post("/create-post", response_class=HTMLResponse)
#async def create_post_submit(request: Request, post_data: PostCreate = Form(...)):
    #db_post = Post(**post_data.dict(), date=datetime.utcnow())
    #db = SessionLocal()
    #db.add(db_post)
    #db.commit()
    #db.refresh(db_post)
    #db.close()
    #return templates.TemplateResponse("post_created.html", {"request": request, "post": db_post})

#@app.get("/view-posts", response_class=HTMLResponse)
#async def view_posts(request: Request):
#    return templates.TemplateResponse("view_posts.html", {"request": request})

#@app.get("/get-posts", response_class=HTMLResponse)
#async def get_posts(username: str = None, date: str = None):
#    db = SessionLocal()
#    query = db.query(Post)
#    if username:
#        query = query.filter(Post.username == username)
#    if date:
#        query = query.filter(Post.date == date)
#    posts = query.all()
#    db.close()
#    return posts


Redirect('/templates/opciones.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
