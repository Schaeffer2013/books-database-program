from models import (Base, session, Book, engine)
#import models
#main menu- add, search, analysis, exit, view
#add books to data base- functions
#edit books
# delete books
#search books
#data cleaning
#loop runs program to exit program and stops


if __name__ == '__main__':
    Base.metadata.create_all(engine)

