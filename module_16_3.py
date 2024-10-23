from fastapi import FastAPI, Path

app = FastAPI()


users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/')
async def main_page() -> str:
    return '~CRUD requests~'


@app.get('/users')
async def main_page() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def new_user(username: str = Path(min_length=5, max_length=20, description="Enter username",example="UrbanUser"), age: int = Path(ge=18, le=120, description='Enter age', example=24)) -> str:
    current_index = int(max(users, key=int))+1
    users[str(current_index)] = f'Имя: {username}, Возраст: {age}'
    return f'User {current_index} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str = Path(min_length=1, max_length=3, description="Enter User ID", example='1'), username: str = Path(min_length=5, max_length=20, description="Enter username",example="UrbanUser"), age: int = Path(ge=18, le=120, description='Enter age', example=24)) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is registered"


@app.delete('/user/{user_id}')
async def delete_user(user_id: str = Path(min_length=1, max_length=3, description="Enter User ID", example='1')):
    users.pop(user_id)




