# Homework-2 >>> AddressBook
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        self.number = value
        super().__init__(value)

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError
        self._number = value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
            # print("Phone added")
        except ValueError:
            print("Phone number must be 10 digits.")

    def remove_phone(self, phone):
        for idx, p in enumerate(self.phones):
            if p.value == phone:
                self.phones.pop(idx)
                print("Phone removed")

    def edit_phone(self, *args):
        try:
            old_phone, new_phone = args
        except ValueError:
            print("Expected 2 arguments.")
        else:
            for idx, p in enumerate(self.phones):
                if p.value == old_phone:
                    try:
                        self.phones[idx] = Phone(new_phone)
                        # print("Phone changed")
                    except ValueError:
                        print("Phone number must be 10 digits.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        try:
            return self.data[name]
        except KeyError:
            print(f"{name} is not found in address book.")

    def delete(self, name):
        try:
            del self.data[name]
            # print(f"{name} removed from the adress book.")
        except KeyError:
            print(f"{name} is not found in address book.")


if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
