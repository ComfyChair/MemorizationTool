from Flashcard import Flashcard
from DbHelper import DbHelper

menu_main_str = "1. Add flashcards\n2. Practice flashcards\n3. Exit"
menu_add_str = "\n1. Add a new flashcard\n2. Exit"
menu_practice_str = 'Please press "y" to see the answer or press "n" to skip:'

db_helper = DbHelper(Flashcard.getBase())

def menu_add():
    while True:
        print(menu_add_str)
        choice = input()
        match choice:
            case "2":
                print()
                return
            case "1":
                q = ""
                while not q.strip():
                    q = input("\nQuestion:\n")
                a = ""
                while not a.strip():
                    a = input("Answer:\n")
                db_helper.add(Flashcard(question=q, answer=a))
            case _:
                print(f"\n{choice} is not an option\n")

def practice():
    flashcards = db_helper.get_all()
    if len(flashcards) == 0:
        print("There is no flashcard.db to practice!")
    else:
        for item in flashcards:
            print(f"\nQuestion: {item.question}")
            while True:
                print(menu_practice_str)
                choice = input().lower()
                match choice:
                    case "y":
                        print(f"\nAnswer: {item.answer}")
                        break
                    case "n":
                        break
                    case _:
                        print(f"\n{choice} is not an option\n")
    print()

def menu_main():
    while True:
        print(menu_main_str)
        choice = input()
        match choice:
            case '1':
                menu_add()
            case '2':
                practice()
            case '3':
                exit_program()
            case _:
                print(f"\n{choice} is not an option\n")

def exit_program():
    db_helper.close()
    print("Bye!")
    exit(0)


if __name__ == '__main__':
    menu_main()