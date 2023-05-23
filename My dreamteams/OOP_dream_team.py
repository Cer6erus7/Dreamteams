# #
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.
#
# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.

# class Soldier:
#     def __init__(self, name):
#         self.name = name
#
#     def shoot(self):
#        print(f"{self.name} тиги-тигитиш!!!")
#
#
# class Guns:
#     def __init__(self, ammo=0):
#         self.ammo = ammo
#
#     def shooting(self):
#         while self.ammo > 0:
#             print("shoot!!!")
#             self.ammo -= 1
#
#     def reload(self, ammo=5):
#         print("Reloading!")
#         self.ammo = ammo
#
#
# class ActOfShooting(Soldier, Guns):
#     def __init__(self, name, ammo=0):
#         Soldier.__init__(self, name)
#         Guns.__init__(self, ammo)
#
#     def soldier_shooting(self):
#         self.shoot()
#         self.shooting()
#         self.reload()
#         self.shooting()
#
#
# actofshooting = ActOfShooting("Rayan", 3)
# actofshooting.soldier_shooting()



# # 2 
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели. В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.


# class Furniture:
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#
#
# class House:
#     def __init__(self, type_of_your_house, max_area=10):
#         self.type_of_your_house = type_of_your_house
#         self.max_area = max_area
#         self.left_area = max_area
#         self.list_of_furniture = []
#
#
#     def add_furniture(self, item: Furniture):
#         if self.left_area >= item.area:
#             self.list_of_furniture.append(item.name)
#             self.left_area -= item.area
#         else:
#              print(f"Not enough space for {item.name}!")
#
#     def __str__(self):
#         return f'Type of house: {self.type_of_your_house}, max area: {self.max_area}, left area: {self.left_area}, furnitures: {self.list_of_furniture}'
#
#
# bed = Furniture("Bed", 3)
# wardrobe = Furniture("Wardrobe", 4)
# bookshelf = Furniture("Bookshelf", 7)
#
# apartment = House("Apartment", 17)
#
# apartment.add_furniture(bed)
# apartment.add_furniture(wardrobe)
# apartment.add_furniture(bookshelf)
#
# print(apartment)


# # 3 
# Students room:
# Реализуйте студенческую комнату с помощью ООП:

# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>


# class Student:
#     def __init__(self, name_of_student, age, language):
#         self.name_of_student = name_of_student
#         self.age = age
#         self.language = language
#
#     def __str__(self):
#         return f"name: {self.name_of_student}, age: {self.age}, language: {self.language}"
#
#
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
#
# print(Steve)
# print(Johnny)
# print(Penny)



# # 4 
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:

# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()

# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3


# class MoneyFmt:
#     def __init__(self, money):
#         self.currency = f"${money:,.2f}"
#
#     def update(self, money):
#         self.currency = f"${money:,.2f}"
#
#     def __repr__(self):
#         if "-" in self.currency:
#             return print(f"-0{self.currency[len(self.currency) - 3:len(self.currency)]}")
#         return print(f"0{self.currency[len(self.currency) - 3:len(self.currency)]}")
#
#     def __str__(self):
#         return self.currency



# # 5  
# Deck of Cards:
# Создайте класс колоды карт. Внутри колода карт должна использовать другой класс - класс карт. Ваши требования:
# Класс Deck должен иметь метод раздачи для раздачи одной карты из колоды.
# После раздачи карты она удаляется из колоды.
# Должен быть метод «смешивания», который проверяет, что в колоде есть все 52 карты, а затем меняет их случайным образом.
# Класс должен иметь масть (червы, бубны, трефы, пики) и ценность карты (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# ПРИМЕЧАНИЕ: используйте случайное перемешивание

# Copy


# from random import shuffle, choice
#
#
# class Card:
#     def __init__(self):
#         self.card = ["A", "2", "3", '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#
#
# class Deck:
#     def __init__(self, card):
#         self.diamonds = [f"{i}♦️" for i in card.card]
#         self.hearts = [f"{i}♥️️" for i in card.card]
#         self.clubs = [f"{i}♠️" for i in card.card]
#         self.spades = [f"{i}♣️️" for i in card.card]
#         self.deck = self.diamonds + self.hearts + self.clubs + self.spades
#
#     def shuffle_card(self):
#         if len(self.deck) == 52:
#             shuffle(self.deck)
#         else:
#             raise "Not all card in the deck"
#
#     def get_card(self):
#         if len(self.deck) > 0:
#             card = choice(self.deck)
#             self.deck.remove(card)
#             return card
#         return "Deck are empty!"
#
#     def __str__(self):
#         print(self.deck)
#         print(len(self.deck))
#
#
# cards = Card()
# decka = Deck(cards)
