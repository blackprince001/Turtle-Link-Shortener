from fastapi import FastAPI
from routes.turtle import turtle_shortener
from routes.admin import admin

app = FastAPI()


@app.get("/")
async def root():
    return (
        "A simple API for shortening links. Infer from the docs right here \
            http://localhost:8000/docs for more!"
    )


app.include_router(turtle_shortener)
app.include_router(admin)