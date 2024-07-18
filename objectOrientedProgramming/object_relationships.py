# Association
# # is a relationship where two objects are related but neither owns the other. 

class Book:
    def __init__(self, title) -> None:
        self.title = title

class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books = [] # store the instance of blueprint Book
    
    def append_book(self, book):
        self.books.append(book)

# Two comms

class Student:

    all = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # teacher is protected because it is not a part of the constructor
        # self._teacher = None
        Student.all.append(self)

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError("Teacher must be an instance of Teacher class")
        self._teacher = value

class Teacher:
    def __init__(self, name):
        self.name = name

    def students(self):
        return [student for student in Student.all if student.teacher == self]

    def add_student(self, student):
        import pdb
        pdb.set_trace()
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of Student class")
        student.teacher = self

# user1 = Student('wassabi', 12)
# user2 = Student('wassabi', 13)
# user3 = Student('wassabi', 14)
# user4 = Student('wassabi', 15)


# print("Student obj",user1)

# teach1 = Teacher("Kimosabi")
# teach2 = Teacher("Kimosabi")

# teach3 = Teacher("Kimosabi")
# teach4 = Teacher("Kimosabi")

# print("Teacher object",teach1.add_student(user1))



# Aggregation
# # is a relationship where one object is a part of another object, 
# and the first object can exist independently.

class Car:
    def __init__(self, model) -> None:
        self.model = model
        self.wheels = []
        self.engine = []

    def add_wheel(self, wheel):
        self.wheels.append(wheel)

    def add_engine(self, engine):
        self.engine.append(engine)

class Engine:
    def __init__(self, cylinders, fuelType):
        self.cylinders = cylinders
        self.fuelType = fuelType

class Wheel:
    def __init__(self, size):
        self.size = size

car = Car("G Wagon")


# Create wheel instances
# wheel1 = Wheel(15)
# wheel2 = Wheel(15)
# wheel3 = Wheel(15)
# wheel4 = Wheel(15)

# four_cylinder_engine = Engine(4, 'regular')



# car.add_wheel(wheel1)
# car.add_wheel(wheel2)
# car.add_wheel(wheel3)
# car.add_wheel(wheel4)

# car.add_engine(four_cylinder_engine)
# print(f'Car: {car.model}')
# for index, item in enumerate(car.wheels, start=1):
#     print(f'Wheel {index}: Size {item.size}')


# Composition
# # is a relationship where one object is made up of another object, 
# and the first object cannot exist without the second object

class Room:
    def __init__(self, name) -> None:
        self.name = name
    
        @property
        def name(self):
                return self._name
        
        @name.setter
        def name(self, value):
            if not value:
                raise ValueError("Name cannot be empty")
            self._name = value

class House:
    def __init__(self, address) -> None:
        self.address = address
        self._rooms = []


    @property
    def rooms(self):
        return self._rooms
    
    def add_room(self, room):
        if not isinstance(room, Room):
            raise ValueError("need to be an instance")
        self._rooms.append(room)


# # Create room instances
# room1 = Room("Living Room")
# room2 = Room("Bedroom")
# room3 = Room("Kitchen")

# # Create a house instance
# house = House("123 Main St")

# # Compose rooms into the house
# house.add_room(room1)
# house.add_room(room2)
# house.add_room(room3)

# # Print the house and its rooms
# print(f'House: {house.address}')
# for room in house.rooms:
#     print(f'  Room: {room.name}')



# Many to many

from datetime import datetime

class Student:

    all = []

    def __init__(self, name):
        self.name = name
        Student.all.append(self)

    def enroll_in_course(self, course):
        Enrollment(self, course)

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.student == self]

    def courses(self):
        return [enrollment.course for enrollment in self.enrollments()]

class Course:

    all = []

    def __init__(self, title):
        self.title = title
        Course.all.append(self)

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.course == self]

    def students(self):
        return [enrollment.student for enrollment in self.enrollments()]

    def enroll_student(self, student):
        Enrollment(student, self)

class Enrollment:

    all = []

    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.enrollment_date = datetime.now()
        Enrollment.all.append(self)
    