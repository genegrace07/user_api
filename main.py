from fastapi import FastAPI
from model import UserDetails

app = FastAPI()

users = [
    UserDetails(id=0,name='luffy',position='captain',salary=100000),
    UserDetails(id=1,name='zorro',position='right hand',salary=80000),
    UserDetails(id=2,name='sanji',position='cook',salary=60000),
    UserDetails(id=3,name='nami',position='navigator',salary=40000),
    UserDetails(id=4,name='yusof',position='sniper',salary=55000)
]

@app.get('/')
def view():
    return users
@app.get('/user_details')
def view2():
    return users
@app.post('/user_details')
def add_user(adduser:UserDetails):
    users.append(adduser)
    return users
@app.get('/user_details/{userid}')
def get_userbyid(userid:int):
    for u in range(len(users)):
        if users[u].id == userid:
            return users[u]
    return 'Not found'
@app.put('/user_details')
def user_update(id:int,new_update:UserDetails):
    for u in range(len(users)):
        if users[u].id == id:
            users[u] = new_update
            return users
    return 'Not found'
@app.delete('/user_details')
def user_delete(userid:int):
    for u in range(len(users)):
        if users[u].id == userid:
            del users[u]
            return users
    return 'Not found'
