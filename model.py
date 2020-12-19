from sqlalchemy import Column, String, Integer
from database import Base, engine


class User(Base):
    __tablename__ = 'user'  # 数据库表名

    user = Column(String(255), primary_key=True, index=True)
    password = Column(String(255), nullable=False)


class Cart(Base):
    __tablename__ = 'cart'
    ID = Column(Integer, primary_key=True, nullable=False)
    number = Column(Integer, nullable=False)


class Merchandise(Base):
    __tablename__ = 'merchandise'
    ID = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    img = Column(String(255), nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
