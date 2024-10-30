import enum

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Enum

Base = declarative_base()

class LeitnerBox(enum.Enum):
    BOX1 = 1
    BOX2 = 2
    BOX3 = 3

    def next(self):
        next_value = (self.value + 1) % 4
        return LeitnerBox(next_value)

class Flashcard (Base):
    __tablename__: str = 'flashcard.db'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    box = Column(Enum(LeitnerBox), default=LeitnerBox.BOX1)

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    @staticmethod
    def getBase():
        return Base
