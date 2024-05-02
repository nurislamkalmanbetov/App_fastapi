from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get('/', description='This is our first route')
async def base_get_route():
    return {"message": "hello world"}


@app.post('/')
async def post():
    return {"message": "hello from the post route"}


@app.put('/')
async def put():
    return {"message": "hello from put method route"}


@app.get('/users')
async def list_users():
    return {"message": "lsit users route"}


@app.get('/users/me')
async def get_current_user():
    return {"Message": "this is the current user"}



@app.get('/users/{user_id}')
async def get_users(user_id: str):
    return {"user_id": user_id} 



class FoodEnum(str, Enum):
    fruits = 'fruits'
    vegetables = 'vegetables'
    dairy = 'dairy'


@app.get('/foods/{food_name}')
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {'food_name': food_name, 'message': 'you are healthy'}
    
    if food_name.value == 'fruits':
        return {
            'food_name': food_name,
            'message': 'you are still healthy, but like sweet thinks'        
            }
    
    return {'food_name': food_name, 'message': 'i like chocolate milk'}