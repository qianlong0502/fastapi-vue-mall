# schemas.py

from pydantic import BaseModel


class User(BaseModel):
    user: str
    password: str
