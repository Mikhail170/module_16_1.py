from fastapi import FastAPI
app = FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {'message': "Главная страница"}

@app.get('/user/admin')
async def welcome() -> dict:
    return {'message': "Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def news(user_id: str) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user')
async def user_info(user_name: str, age: int) -> dict:
     return {'Информация о пользователе': user_name, "Возраст": age}



