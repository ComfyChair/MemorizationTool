from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from Flashcard import Flashcard, LeitnerBox


class DbHelper:
    def __init__(self, db_name: str, schema: DeclarativeBase):
        engine = create_engine(f'sqlite:///{db_name}?check_same_thread=False')
        schema.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add(self, element):
        session = self.session
        session.add(element)
        session.commit()

    def update(self, card_id, question, answer):
        session = self.session
        (session.query(Flashcard).filter_by(id=card_id)
         .update({ "question": question, "answer": answer}))
        session.commit()

    def updateBox(self, id: int, box: LeitnerBox):
        session = self.session
        session.query(Flashcard).filter_by(id=id).update({ "box": box })
        session.commit()

    def delete(self, card_id):
        session = self.session
        session.query(Flashcard).filter_by(id=card_id).delete()
        session.commit()

    def get_all(self) -> list:
        session = self.session
        return session.query(Flashcard).all()

    def close(self):
        self.session.close()

