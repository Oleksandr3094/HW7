from collections import UserDict
import datetime as dt
from datetime import datetime as dtdt

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
	pass

class Phone(Field):
    def __init__(self, value):
        phone_str = str(value)
        if not (phone_str.isdigit() and len(phone_str) == 10):
            raise ValueError("Номер телефону повинен складатися рівно з 10 цифр.")
        super().__init__(phone_str)

class Birthday(Field):
    def __init__(self, value):
        try:
            parsed_date = dtdt.strptime(value.strip(), "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Невірний формат дати. Використовуйте ДД.ММ.РРРР.")
        super().__init__(parsed_date)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        found_phone = self.find_phone(phone)
        if not found_phone:
            raise ValueError(f"Номер {phone} не знайдено.")
        self.phones.remove(found_phone)

    def edit_phone(self, old_phone, new_phone):
        validated_phone = Phone(new_phone)  # Перевіряє new_phone на 10 цифр; при помилці кине ValueError
        found_phone = self.find_phone(old_phone)
        if not found_phone:
            raise ValueError(f"Старий номер {old_phone} не знайдено.")
        found_phone.value = validated_phone.value

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
          
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value if self.birthday else 'Not specified'}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def birthdays_this_week(self, days: int = 7):
        today = dtdt.today().date()
        end_date = today + dt.timedelta(days=days)
        birthdays = []

        for record in self.data.values():
            if not record.birthday:
                continue

            birthday = record.birthday.value
            try:
                greeting_date = birthday.replace(year=today.year)
            except ValueError:
                # підстраховка для 29.02 у не високосному році
                greeting_date = birthday.replace(year=today.year, month=2, day=28)

            if greeting_date < today:
                try:
                    greeting_date = birthday.replace(year=today.year + 1)
                except ValueError:
                    greeting_date = birthday.replace(year=today.year + 1, month=2, day=28)

            # Переносимо суботу (5) і неділю (6) на понеділок (0)
            if greeting_date.weekday() == 5:
                greeting_date += dt.timedelta(days=2)
            elif greeting_date.weekday() == 6:
                greeting_date += dt.timedelta(days=1)

            if today <= greeting_date <= end_date:
                birthdays.append((record.name.value, greeting_date.strftime("%d.%m.%Y")))

        return birthdays
            
