from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

from routes.admin import admin
import routes.user as UserRoute

# from turtle_link_shortener.errors import UserNotFound, IncorrectPassword
# from turtle_link_shortener.models import User as UserModel
# from turtle_link_shortener.security import Password

# from sqlalchemy import select
# from sqlalchemy.orm import Session

# from utils.database_utils import get_db
# from schemas.user import UserCreate, UserBase

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    content = """
        <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>A simple API for shortening links. Infer from the docs right here \
            <a href=/docs> Docs </a> for more!</h1>
        </body>
    </html> """
    return HTMLResponse(content=content, status_code=status.HTTP_200_OK)


# @app.get("/signup")
# async def signup(new_user: UserCreate, db: Session = Depends(get_db)):
#     return create_user(new_user, db=db)


# @app.get("/login")
# async def login(existing_user: UserBase, db: Session = Depends(get_db)):
#     db_user = db.scalar(
#         select(UserModel).where(UserModel.username == existing_user.username)
#     )
#     if db_user is None:
#         raise UserNotFound(
#             status_code=404,
#             detail=f"No User with username={existing_user.username} found!",
#         )

#     if not Password.verify(existing_user.password, db_user.password):
#         raise IncorrectPassword(
#             status_code=404, detail="Password must be wrong, try again later!"
#         )

#     return db_user


app.include_router(admin)
app.include_router(router=UserRoute.user)
