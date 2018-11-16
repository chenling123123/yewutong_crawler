from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine('mysql+pymysql://root:root@localhost:3306/ywt?charset=utf8')
Base = declarative_base()

class Ywt(Base):
    __tablename__ = 'ywt_table111'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    creating_date = Column(String(64))

    address_img_url = Column(String(255))
    phone_img_url = Column(String(255))

    img_urls = Column(String(255))
    images = Column(String(255))


if __name__ == '__main__':
    Base.metadata.create_all(engine)