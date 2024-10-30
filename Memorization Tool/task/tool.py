from Flashcard import Flashcard
from Flashcard import LeitnerBox
from DbHelper import DbHelper
from typing import List

MENU_MAIN = '1. Add flashcards\n2. Practice flashcards\n3. Exit'
MENU_ADD = '\n1. Add a new flashcard\n2. Exit'
MENU_PRACTICE = 'press "y" to see the answer:\npress "n" to skip:\npress "u" to update:'
MENU_UPDATE = 'press "d" to delete the flashcard:\npress "e" to edit the flashcard:'
MENU_LEARNING = 'press "y" if your answer is correct:\npress "n" if your answer is wrong:'

db_helper = DbHelper("flashcard.db", Flashcard.getBase())

def invalid(choice: str) -> str:
    return f"\n{choice} is not an option\n"

def menu_add():
    while True:
        print(MENU_ADD)
        choice = input()
        match choice:
            case "1":
                q = ""
                while not q.strip():
                    q = input("\nQuestion:\n")
                a = ""
                while not a.strip():
                    a = input("Answer:\n")
                db_helper.add(Flashcard(question=q, answer=a))
            case "2":
                print()
                return
            case _:
                print(invalid(choice))

def menu_update(card: Flashcard):
    while True:
        print(MENU_UPDATE)
        choice = input().lower()
        match choice:
            case "d":
                db_helper.delete(card.id)
                return  # back to practice
            case "e":
                print(f"current question: {card.question}")
                new_q = input("please write a new question:\n")
                if not new_q.strip():
                    new_q = card.question
                print(f"current answer: {card.answer}")
                new_a = input("please write a new answer:\n")
                if not new_a.strip():
                    new_a = card.answer
                db_helper.update(card.id, new_q, new_a)
                return  # back to practice
            case _:
                print(invalid(choice))

def practice():
    flashcards : List[Flashcard] = db_helper.get_all()
    if len(flashcards) == 0:
        print("There is no flashcard to practice!")
    else:
        for card in flashcards:
            print(f"\nQuestion: {card.question}")
            menu_practice(card)
    print()

def menu_learning(card : Flashcard):
    while True:
        print(MENU_LEARNING)
        choice = input().lower()
        match choice:
            case "y":
                if card.box is LeitnerBox.BOX3:
                    db_helper.delete(card.id)
                else:
                    db_helper.updateBox(card.id, card.box.next())
                return
            case "n":
                if card.box.value > LeitnerBox.BOX1.value:
                    db_helper.updateBox(card.id, LeitnerBox.BOX1)
                return
            case _:
                print(invalid(choice))

def menu_practice(card):
    while True:
        print(MENU_PRACTICE)
        choice = input().lower()
        match choice:
            case "y":
                print(f"\nAnswer: {card.answer}")
                menu_learning(card)
                return
            case "n":
                return
            case "u":
                menu_update(card)
                return
            case _:
                print(invalid(choice))

def menu_main():
    while True:
        print(MENU_MAIN)
        choice = input()
        match choice:
            case '1':
                menu_add()
            case '2':
                practice()
            case '3':
                exit_program()
            case _:
                print(invalid(choice))

def exit_program():
    db_helper.close()
    print("Bye!")
    exit(0)


if __name__ == '__main__':
    menu_main()