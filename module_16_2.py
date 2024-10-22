from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def welkome():
    return "Главная страница"


@app.get("/user/admin")
async def welkome():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def welkome(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=1)):
    return f"Вы вошли как пользователь №: {user_id}"


@app.get("/user/{username}/{age}")
async def welkome(username: str = Path(min_length=5, max_length=20, description="Enter username",example="UrbanUser"), age: int = Path(ge=18, le=120, description='Enter age', example=24)):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


@app.get("/user_nick/{nickname}/{game_rating}")
async def welkome(nickname: Annotated[str, Path(min_length=5, max_length=10, description="Enter nickname",example="UrbanNick")], game_rating: int):
    return f"Информация о пользователе. Никнейм: {nickname}, Рейтинг: {game_rating}"