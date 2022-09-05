# Password Generator Project
import random


class PasswordGenerator:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        self.nr_letters = random.randint(3, 7)
        self.nr_symbols = random.randint(1, 3)
        self.nr_numbers = random.randint(1, 3)
        self.password_list = []

    def create(self):
        for char in range(self.nr_letters):
            self.password_list.append(random.choice(self.letters))
        for char in range(self.nr_symbols):
            self.password_list += random.choice(self.symbols)
        for char in range(self.nr_numbers):
            self.password_list += random.choice(self.numbers)
        random.shuffle(self.password_list)
        password = ""
        for char in self.password_list:
            password += char

        return password
