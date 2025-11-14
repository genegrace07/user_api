from pydantic import BaseModel

class UserDetails(BaseModel):
    id:int
    name:str
    position:str
    salary:int
