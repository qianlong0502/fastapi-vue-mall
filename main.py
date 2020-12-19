from fastapi import FastAPI, Depends
from typing import Optional
from pydantic import BaseModel
import hashlib
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from database import SessionLocal
import model
import schemas


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ResponseModel(BaseModel):
    error: int = 0
    tip: str = ''


class ResponseCart(BaseModel):
    data: list = []


app = FastAPI()

# serve static files
app.mount("/static", StaticFiles(directory="static"), name="index.html")
app.mount("/static", StaticFiles(directory="static"), name="cart.html")


@app.post("/login/")
def login(user: schemas.User, db: Session = Depends(get_db)):
    user_dict = user.dict()
    query = db.query(model.User).filter(model.User.user == user_dict['user']).first()
    if query is None:
        return ResponseModel(error=0, tip='该用户不存在！')
    else:
        md5 = hashlib.md5()
        md5.update(bytes(user_dict['password'], encoding='utf-8'))
        password_md5 = md5.hexdigest()
        if password_md5 == query.password:
            return ResponseModel(error=1, tip='登陆成功！')
        else:
            return ResponseModel(error=0, tip='密码错误！')


@app.post("/register/")
def login(user: schemas.User, db: Session = Depends(get_db)):
    user_dict = user.dict()
    query = db.query(model.User).filter(model.User.user == user_dict['user']).first()
    if query is not None:
        return ResponseModel(error=0, tip="用户已经存在！")
    username = user_dict['user']
    md5 = hashlib.md5()
    md5.update(bytes(user_dict['password'], encoding='utf-8'))
    password_md5 = md5.hexdigest()
    raw = model.User(user=username, password=password_md5)
    try:
        db.add(raw)
        db.commit()
        db.refresh(raw)
        return ResponseModel(error=1, tip="注册成功！")
    except:
        return ResponseModel(error=0, tip="数据库出错！")


@app.get("/cart")
def cart(db: Session = Depends(get_db)):
    Carts = db.query(model.Cart).all()
    cartList = []
    for aCart in Carts:
        obj = {}
        aMerchandise = db.query(model.Merchandise).filter(model.Merchandise.ID == aCart.ID).first()
        obj['id'] = aCart.ID
        obj['name'] = aMerchandise.name
        obj['price'] = aMerchandise.price
        obj['img'] = aMerchandise.img
        obj['count'] = aCart.number
        cartList.append(obj)
    return ResponseCart(data=cartList)
