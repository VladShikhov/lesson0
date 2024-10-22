from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def welkome():
    return "Главная страница"


@app.get("/user/admin")
async def welkome():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def welkome(user_id):
    return f"Вы вошли как пользователь №: {user_id}"


@app.get("/user")
async def welkome(username='name', age=0):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


