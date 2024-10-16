from fastapi import FastAPI
from app.controller import user_controller

app = FastAPI()
app.include_router(user_controller.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/user/{user_id}")
# async def get_user(user_id: int):
#     return await uc.get_user(user_id)