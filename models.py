#create a database
#books.db
#create a model
#title, author, data published, price





from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///books.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column('Title', String)
    author = Column('Author', String)
    published_date = Column('Publsihed', Date)
    price = Column('Price', Integer)
    

    def __repr__(self):
        return f'Title: {self.title} Author: {self.author} Publsihed: {self.published_date} Price: {self.price}'
    

if __name__ == '__main__':
    Base.metadata.create_all(engine)

