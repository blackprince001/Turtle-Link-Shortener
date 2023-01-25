from fastapi import FastAPI
from routes.admin import admin
from routes.user import user

app = FastAPI()


@app.get("/")
async def root():
    return (
        "A simple API for shortening links. Infer from the docs right here \
            http://localhost:8000/docs for more!"
    )


app.include_router(admin)
app.include_router(user)
