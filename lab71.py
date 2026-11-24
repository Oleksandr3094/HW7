# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Point(x={self.x}, y={self.y})"


# original_point = Point(2, 3)
# print(original_point) 

# # Використання рядка, повернутого __repr__, для створення нового об'єкта
# new_point = eval(repr(original_point))
# print(new_point)

# class Human:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Human named {self.name} who is {self.age} years old"
    
#     def __repr__(self):
#         return f"Human({self.name}, {self.age})"

# human = Human("Alice", 30)
# print(human)

# class SimpleDict:
#     def __init__(self):
#         self.__data = {}

#     def __getitem__(self, key):
#         return self.__data.get(key, "Key not found")

#     def __setitem__(self, key, value):
#         self.__data[key] = value

# # Використання класу
# simple_dict = SimpleDict()
# simple_dict['name'] = 'Boris'
# print(simple_dict['name'])   # Виводить: Boris
# print(simple_dict['age'])   # Виводить: Key not found

# class BoundedList:
#     def __init__(self, min_value: int, max_value: int):
#         self.min_value = min_value
#         self.max_value = max_value
#         self.__data = []

#     def __getitem__(self, index: int):
#         return self.__data[index]

#     def __setitem__(self, index: int, value: int):
#         if not (self.min_value <= value <= self.max_value):
#             raise ValueError(f"Value {value} must be between {self.min_value} and {self.max_value}")
#         if index >= len(self.__data):
#             # Додати новий елемент, якщо індекс виходить за межі
#             self.__data.append(value)
#         else:
#             # Замінити існуючий елемент
#             self.__data[index] = value

#     def __repr__(self):
#         return f"BoundedList({self.max_value}, {self.min_value})"

#     def __str__(self):
#         return str(self.__data)

# if __name__ == '__main__':
#     temperatures = BoundedList(18, 26)

#     for i, el in enumerate([20, 22, 25, 27]):
#         try:
#             temperatures[i] = el
#         except ValueError as e:
#             print(e)

#     print(temperatures)

# from collections import UserList

# class BoundedList(UserList):
#     def __init__(self, min_value: int, max_value: int, initial_list=None):
#         super().__init__(initial_list if initial_list is not None else [])
#         self.min_value = min_value
#         self.max_value = max_value
#         self.__validate_list()

#     def __validate_list(self):
#         for item in self.data:
#             self.__validate_item(item)

#     def __validate_item(self, item):
#         if not (self.min_value <= item <= self.max_value):
#             raise ValueError(f"Item {item} must be between {self.min_value} and {self.max_value}")

#     def append(self, item):
#         self.__validate_item(item)
#         super().append(item)

#     def insert(self, i, item):
#         self.__validate_item(item)
#         super().insert(i, item)

#     def __setitem__(self, i, item):
#         self.__validate_item(item)
#         super().__setitem__(i, item)

#     def __repr__(self):
#         return f"BoundedList({self.max_value}, {self.min_value})"

#     def __str__(self):
#         return str(self.data)

# if __name__ == '__main__':
#     temperatures = BoundedList(18, 26, [19, 21, 23])
#     print(temperatures)

#     for el in [20, 22, 25, 27]:
#         try:
#             temperatures.append(el)
#         except ValueError as e:
#             print(e)

#     print(temperatures)

# from collections import UserDict

# class MyDict(UserDict):
#     def __add__(self, other):
#         temp_dict = self.data.copy()
#         temp_dict.update(other)
#         return MyDict(temp_dict)

#     def __sub__(self, other):
#         temp_dict = self.data.copy()
#         for key in other:
#             if key in temp_dict:
#                 temp_dict.pop(key)
#         return MyDict(temp_dict)

# if __name__ == '__main__':
#     d1 = MyDict({1: 'a', 2: 'b'})
#     d2 = MyDict({3: 'c', 4: 'd'})

#     d3 = d1 + d2
#     print(d3)

#     d4 = d3 - d2
#     print(d4)

# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def __add__(self, other):
#         return ComplexNumber(self.real + other.real, self.imag + other.imag)

#     def __sub__(self, other):
#         return ComplexNumber(self.real - other.real, self.imag - other.imag)

#     def __mul__(self, other):
#         real_part = self.real * other.real - self.imag * other.imag
#         imag_part = self.real * other.imag + self.imag * other.real
#         return ComplexNumber(real_part, imag_part)

#     def __str__(self):
#         return f"{self.real} + {self.imag}i"

# if __name__ == "__main__":
#     num1 = ComplexNumber(1, 2)
#     num2 = ComplexNumber(3, 4)
#     print(f"Сума: {num1 + num2}")
#     print(f"Різниця: {num1 - num2}")
#     print(f"Добуток: {num1 * num2}")

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def __eq__(self, other):
#         if not isinstance(other, Rectangle):
#             return NotImplemented
#         return self.area() == other.area()

#     def __ne__(self, other):
#         return not self.__eq__(other)

#     def __lt__(self, other):
#         if not isinstance(other, Rectangle):
#             return NotImplemented
#         return self.area() < other.area()

#     def __le__(self, other):
#         return self.__lt__(other) or self.__eq__(other)

#     def __gt__(self, other):
#         if not isinstance(other, Rectangle):
#             return NotImplemented
#         return self.area() > other.area()

#     def __ge__(self, other):
#         return self.__gt__(other) or self.__eq__(other)

# if __name__ == "__main__":
#     rect1 = Rectangle(5, 10)
#     rect2 = Rectangle(3, 20)
#     rect3 = Rectangle(5, 10)
#     print(f"Площа прямокутників: {rect1.area()}, {rect2.area()}, {rect3.area()}")
#     print(rect1 == rect3)  # True: площі рівні
#     print(rect1 != rect2)  # True: площі не рівні
#     print(rect1 < rect2)  # True: площа rect1  менша, ніж у rect2
#     print(rect1 <= rect3)  # True: площі рівні, тому rect1 <= rect3
#     print(rect1 > rect2)  # False: площа rect1 менша, ніж у rect2
#     print(rect1 >= rect3)  # True: площі рівні, тому rect1 >= rect3

class Person:
    def __init__(self, age):
        self.__age = age  # Пряме присвоєння значення атрибуту в конструкторі

    @property
    def age(self):
        return self.__age  # Геттер повертає значення приватного поля

    @age.setter
    def age(self, value):
        if value < 0:
            # Валідація вхідного значення
            raise ValueError("Вік не може бути від'ємним")  
        # Присвоєння валідного значення приватному полю
        self.__age = value  

if __name__ == "__main__":
    person = Person(10)
    print(person.age)
    person.age = -5 # Викличе ValueError: Вік не може бути від'ємним

class Person:
    def __init__(self, age):
        # Спочатку встановлюємо __age як None
        self.__age = None
        # Використовуємо сеттер для встановлення віку, що дозволяє валідацію вхідного значення
        self.age = age

    @property
    def age(self):
        # Геттер повертає значення приватного поля
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            # Валідація вхідного значення
            raise ValueError("Вік не може бути від'ємним")
        # Присвоєння валідного значення приватному полю
        self.__age = value

if __name__ == "__main__":
    person = Person(-10)
    print(person.age)

