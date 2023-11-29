from flask import Flask
import connexion




app = Flask(__name__)
api = connexion.App(__name__, specification_dir='../openapi/')
api.add_api('openapi.yaml')
api.init_app(app)


@app.route('/')
def home():
    return 'Welcome to my Flask server!'

@app.route('/api/some_endpoint', methods=['GET'])
def some_endpoint():
    # Your logic here
    return 'This is a response from the API endpoint.'



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
