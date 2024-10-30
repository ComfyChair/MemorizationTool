from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Flashcard (Base):
    __tablename__: str = 'flashcard.db'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    @staticmethod
    def getBase():
        return Base
