from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Flashcard import Flashcard

class DbHelper:
    def __init__(self, Base):
        engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
        Base.metadata.create_all(engine)
        # connection = engine.connect()
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add(self, element):
        session = self.session
        session.add(element)
        session.commit()

    def get_all(self) -> list:
        session = self.session
        return session.query(Flashcard).all()

    def close(self):
        self.session.close()
