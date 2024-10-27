from fastapi import FastAPI
from app.controller import user_controller

app = FastAPI()
app.include_router(user_controller.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}