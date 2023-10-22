# Homework-2 >>> CLI-bot
class NameExistsError(Exception):
    pass


class EmptyContactsError(Exception):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Wrong format! Correct format in the help."
        except KeyError:
            return "Name not found."
        except IndexError:
            pass
        except NameExistsError:
            return "Name already exists."
        except EmptyContactsError:
            return "Contact list is empty."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    if contacts.get(name) != None:
        raise NameExistsError
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    current_phone = contacts[name]
    contacts[name] = phone
    return "Contact changed."


@input_error
def show_phone(args, contacts):
    name, = args
    return contacts[name]


@input_error
def show_all(contacts):
    contact_list = []
    if len(contacts) == 0:
        raise EmptyContactsError
    for k, v in contacts.items():
        contact_list.append(k + ": " + v)
    return ("\n").join(contact_list)


def show_all_commands():
    commands = {"add": "add [name] [phone]",
                "change": "change [name] [phone]",
                "phone": "phone [name]",
                "all": "all",
                "help": "help",
                "exit": "exit"}
    command_list = []
    for k, v in commands.items():
        line = "{:<9}{:<5}{:<25}".format(k, ">>>", v)
        command_list.append(line)
    return ("\n").join(command_list)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi"]:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'help':
            print(show_all_commands())
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
