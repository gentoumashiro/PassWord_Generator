from random import shuffle, randint
from secrets import choice
from time import time

from pyperclip import copy

names_list = [
    'Julius Harrison', 'Rocco Varndell', 'Blake Thomson', 'Camila Robinson', 'Sydney Sherry', 'Nathan Roberts',
    'Ada Flack', 'Adalind Lloyd', 'Adalie Emmett', 'Johnathan Ripley', 'Jacob Lee', 'Esmeralda Maxwell',
    'Michael Franks', 'Noah Wooldridge', 'Daniel Poole', 'Joseph Price', 'Elena Barclay', 'Michael Todd',
    'Eileen Evans', 'Sebastian Chapman', 'George Mann', 'Destiny Alldridge', 'Aiden Lewis', 'Harvey Thomson',
    'Rosalyn Mcleod', 'Matt Ranks', 'Leilani Nicholls', 'Harry Garner', 'Maggie Wilcox', 'Michael Stevens',
    'Iris Rothwell', 'Maia Gilmore', 'Carter Devonport', 'Adalind Pope', 'Chadwick Edwards', 'Sarah Rivers',
    'Candace Wilkinson', 'William Dickson', 'Freya Ward', 'Sasha Rossi', 'Clint Tait', 'Ryan Thomas',
    'Rick Boden', 'Elena Anderson', 'Morgan Larkin', 'Josh Boden', 'Nancy Gosling', 'Hayden Groves',
    'Aisha Simpson', 'Erick Sheldon', 'Caydence Aldridge', 'Gabriel Whinter', 'Ryan Wise', 'Sloane Thorne',
    'Melania Garcia', 'Maggie Taylor', 'Enoch Reading', 'Kendra Holt', 'Bob Harris', 'Ron Ebden',
    'Lillian Potts', 'Angel Ripley', 'Stacy Gonzales', 'Harry Ellis', 'Enoch Adler', 'Cedrick Broomfield',
    'Jane Cox', 'Julian Yarlett', 'Phillip Pearce', 'Emerald Whitehouse', 'Tyler Clayton', 'Peter Chapman',
    'Caleb Dunbar', 'Alessia Barclay', 'Luke Varndell', 'Nicholas Tobin', 'Barney Wood', 'Janice Mitchell',
    'Ciara Walter', 'Jade Chadwick', 'Gil Eaton', 'Carter Marshall', 'Bree Mills', 'Nancy Gavin',
    'Johnathan Woodley', 'Crystal Ellis', 'Sebastian Devonport', 'Fred Appleton', 'Hank Bingham',
    'Esmeralda Redwood', 'Kenzie Higgs', 'Bryon Evans', 'Ethan Giles', 'Joseph Kaur', 'Candace Johnson',
    'Mark Irving', 'Sharon Blythe', 'Daniel Wright', 'Olivia Stone', 'Jack Benfield'
]


def generate_password(alph: str) -> str:
    password = [choice(alph) for _ in range(randint(13, 30))]
    return ''.join(password)


def symbols_alphabet() -> str:
    letters = list(set(['!@#$%^&*()'] + [chr(i) for i in range(48, 126)]))
    shuffle(letters)
    return ''.join(letters)


def copy_to_clipboard(data) -> copy:
    return copy(data)


def generate_data() -> str:
    letters = symbols_alphabet()
    password = generate_password(letters)
    name = choice(names_list)
    mail = name[:15].replace(' ', '_') + 'as12388@gmail.com'
    result = f"{name}\n{mail}\n{password}"
    return result


def save_document(data, i) -> None:
    with open(f'{i} {time()}.txt', 'w', encoding='UTF-8') as file:
        file.write(data)


def main(i: int = 1):
    data = generate_data()
    save_document(data, i)
    copy_to_clipboard(data)


if __name__ == '__main__':
    try:
        main()
        print("[✅] Password was copied to clipboard and file.txt was created[✅]")

    except Exception as ex:
        print(f"[❌] Something went wrong, try to reboot programm! [❌]\nОшибка: '{ex}")
