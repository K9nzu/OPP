# البرمجة الكائنية (Object Oriented Programming)
# z = 5
# print (type(z))
#-----------------
# n = 'Ammar'
# print (type(n))
#-----------------
# b = True
# print (type(b))
#-----------------
# t = (3,6,1)
# print (type(t))
#-----------------
# d = {'A' : 'Ammar'}
# print (type(d))
#-----------------
# n = 'Ammar'
# print (n.upper()) # لجعل الكلمة كلها احرف كبيرة
#-----------------
class Student:
    no_to_student = 0
    def __init__(self, name, age=0, rating='none'):
        self.name = name
        self.age = age
        self.rating = rating
        Student.no_to_student += 1

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name
    
    def describe(self):
        print (f'my name is {self.name} and my age is {self.age}') 
        print ('my name is {} and my age is {}'.format(self.name,self.age)) #نفس الكود الفوق بختلاف بسيط

    def num_old(self , nage):
        if self.age <= nage:
            print ('is not old')
        else:
            print ('is old')
        
student_1 = Student ("Ahmed")
student_2 = Student ('Noor', 24, 6)
student_3 = Student ('Ammar', 45, [8,'Good'])

# print (student_3.get_name())
# student_3.set_name('ibrahim')
# print (student_3.get_name())

# student_2.num_old(40)
# student_3.num_old(40)
# student_2.describe()
# student_3.describe()

# print(id(student_1) == id(student_2))
# print (student_1.age, student_3.rating)
# student_2.name = 'Farah'
# student_1.age = 18
# print (student_1.age, student_2.name)
# print (student_1.no_to_student, student_2.no_to_student, student_3.no_to_student) # يحسب عدد الستيودنت
# print (Student.no_to_student) # ايضا يحسب عدد الكلاس او الستيودنت


#-----------------
class Student:
    no_to_student = 0
    def __init__(self, name, age=0, rating='none'):
        self.__name = name # تحويل الستيت ل برايفت من خلال __ تو اندر سكور
        self.__age = age
        self.__rating = rating

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

    def describe(self):
        print (f'my name is {self.__name} and my age is {self.__age}') 
        print ('my name is {} and my age is {}'.format(self.__name,self.__age)) #نفس الكود الفوق بختلاف بسيط

    def num_old(self , nage):
        if self.__age <= nage:
            print ('is not old')
        else:
            print ('is old')

student_4 = Student('samer', 35, 2)
# student_4.__name = 'zina' # لا نستطيع تغيير النيم اذا كان برايفت الستيت
# print (student_4.__name) # الى في حال كتبت بهذا الشكل
# print (student_4.get_name())

# student_4.set_name('zain')
# student_4.set_age(55)
# student_4.describe()

# student_4.__age = 42
# student_4.describe()

#-----------------
# (Classmethod)
from datetime import date
class Student:
    no_to_student = 0
    def __init__(self, name, age=0):
        self.__name = name # تحويل الستيت ل برايفت من خلال __ تو اندر سكور
        self.__age = age

    def describe(self):
        print (f'my name is {self.__name} and my age is {self.__age}') 
        # print ('my name is {} and my age is {}'.format(self.__name,self.__age)) #نفس الكود الفوق بختلاف بسيط

    @classmethod
    def initFromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

student_5 = Student('samer', 49)
student_6 = Student.initFromBirthYear('Ammar', 2005)
# student_6.describe()
# student_5.describe()

#-----------------
# (Classmethod)
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def veg(cls):
        return cls(['mushrooms', 'olives', 'onions'])

    @classmethod
    def margherita(cls):
        return cls(['mozarella', 'sauce'])

    def __str__(self):
        return f'Pizza ingredients are {self.ingredients}'
        

pizza1 = Pizza(['tomatoes', "olives"])
pizza2 = Pizza.veg()
pizza3 = Pizza.margherita()
# print (pizza2, pizza3, pizza1)
# print (dir(Pizza))

#-----------------
# (Staticmethod)
class Math:
    @staticmethod
    def add(x,y):
        return x + y

    @staticmethod
    def add5(num):
        return num + 5

    @staticmethod
    def add10(num):
        return num + 10

    @staticmethod
    def PI():
        return 3.14

x = Math.add(5 , 10)
y = Math.add5(x)
z = Math.add10(y)
# print (x,y,z)

#-----------------
# (Staticmethod)
class Pizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __str__(self):
        return f'Pizza ingredients are {self.ingredients}'

    def area(self):
        return Pizza.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * Math.PI()

p = Pizza(6, ['mozzarella', 'tomatoes'])
# print (p.area())
# print (Pizza.circle_area(4))

#-----------------
class Dates:
    def __init__(self, date):
        self.__date = date

    def getDate(self):
        return self.__date

    @staticmethod
    def toDashDate(date):
        return date.replace('/','-')

date = Dates('15-12-2016')
dateFromDB = '15/12/2016'
dateWithDash = Dates.toDashDate(dateFromDB)

# if (date.getDate() == dateWithDash):
#     print ('Equal')
# else:
#     print ('Unequal')

#-----------------
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"name is {self.name} age is {self.age} "

    @classmethod
    def initFromBirthYear(cls, name, birthYear, extra):
        return cls(name, date.today().year - birthYear, extra)

class Man(Person):
    gender = "Male"
    no_of_man = 0

    def __init__(self, name, age, voice):
        super().__init__(name, age)
        self.voice = voice
        Man.no_of_man += 1

    def display(self):
        string = super().display()
        return string + f'and voice is {self.voice} and gender is {self.gender}'

man = Man('Ammar', 66, 'hard')
# print (man.display())
# print (Man.no_of_man)

class Woman(Person):
    gender = "Female"
    no_of_woman = 0

    def __init__(self, name, age, hair):
        super().__init__(name, age)
        self.hair = hair
        Woman.no_of_woman += 1

    def display(self):
        string = super().display()
        return string + f'and voice is {self.hair} and gender is {self.gender}'

woman = Woman('Noor', 33, 'curly')
# print (woman.display())
# print (Woman.no_of_woman)

man = Man.initFromBirthYear('Abdallah', 2015, 'hard')
# print (man.display())

woman = Woman.initFromBirthYear('Farah', 2000, 'curly')
# print (woman.display())

# print (isinstance(woman, Woman))
# print (isinstance(woman, Man))
# print (isinstance(man, Person))
#-----------------
# (Abstractmethod)
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4

class Rect(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return (self.__length + self.__width) * 2

square = Square(10)
# print (f'square area is {square.area()} and perimeter is {square.perimeter()}')
rect = Rect(5 , 3)
# print (f'rectangle area is {rect.area()} and perimeter is {rect.perimeter()}')

#-----------------
class Man():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __add__(self, other):
        names = self.name + ' and ' + other.name
        ages = self.age + other.age
        return f'name combined are {names} and sum of ages is {ages}'

    def __lt__(self, other):
        return self.age < other.age


    def display(self):
        return f'name is {self.name} and age is {self.age}'

man = Man('islam', 17)
man2 = Man('Ahmed', 26)
# print (man+man2)
# print (man<man2)

#                                    و خلصنه الحمد الله البرمجة الكائنية (OPP)
#                                                     The End

