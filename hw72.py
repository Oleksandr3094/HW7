from functools import wraps
from hw7 import AddressBook, Record


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e) or "Некоректне значення."
        except KeyError as e:
            return str(e).strip("'") or "Контакт не знайдено."
        except IndexError:
            return "Недостатньо аргументів для команди."
        except Exception as e:
            return f"Неочікувана помилка: {e}"
    return inner


@input_error
def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args
    
@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Вкажіть ім'я та телефон. Формат: add <ім'я> <10_цифр>")
    name, phone,*_ = args
    record = book.find(name)
    message = "Контакт оновлено."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Контакт додано."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook) -> str:
    if len(args) < 3:
        raise ValueError("Вкажіть ім'я, старий і новий номер. Формат: change <ім'я> <старий_номер> <новий_номер>")
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError(f"Контакт '{name}' не знайдено.")
    record.edit_phone(old_phone, new_phone)
    return "Контакт оновлено."

@input_error
def show_phone(args, book: AddressBook):
    if not args:
        return "Вкажіть ім'я контакту. Формат: phone <ім'я>"
    name = args[0]
    record = book.find(name)
    if record is None:
        return f"Контакт '{name}' не знайдено."
    if not record.phones:
        return f"У контакту '{name}' ще немає збережених телефонів."
    return "; ".join(str(phone) for phone in record.phones)

@input_error
def show_all(args, book: AddressBook) -> str:
    if not book:
        return "Адресна книга порожня."
    lines = [f"{name:<15}: {record}" for name, record in book.items()]
    return "\n".join(lines)

@input_error
def add_birthday(args, book: AddressBook) -> str:
    if len(args) < 2:
        return "Вкажіть ім'я та дату народження. Формат: add-birthday <ім'я> <DD.MM.YYYY>"
    name, birthday, *_ = args
    user_record = book.find(name)  
    if user_record is None:
        return f"Контакт '{name}' не знайдено."
    user_record.add_birthday(birthday)
    return "День Народження додано."

@input_error
def show_birthday(args, book: AddressBook) -> str:
    if not args:
        return "Вкажіть ім'я контакту. Формат: show-birthday <ім'я>"
    name = args[0]
    record = book.find(name)  
    if record is None:
        return f"Контакт '{name}' не знайдено."
    if record.birthday is None:
        return f"Для контакту '{name}' день народження не вказано."
    return record.birthday.value.strftime("%d.%m.%Y")
    

@input_error
def birthdays(args, book: AddressBook) -> str:
    upcoming = book.birthdays_this_week()
    if not upcoming:
        return "Найближчих днів народження немає."
    lines = [f"{name:<15} — {birthday}" for name, birthday in upcoming]
    return "\n".join(lines)

def main():
    book = AddressBook()
    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "add-birthday": add_birthday,
        "show-birthday": show_birthday,
        "birthdays": birthdays,
    }

    print("Вітаю в асистент боті!")

    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Бувай!")
            break

        if command == "":
            continue

        if command == "hello":
            print("Чим я можу допомогти?")
            continue

        handler = commands.get(command)
        if handler is None:
            print("Невідома команда.")
            continue

        print(handler(args, book))

if __name__ == "__main__":
    main()