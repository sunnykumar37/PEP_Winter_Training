from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
    profession: str
p1 = Person("Alice", 25, "Engineer")
print(p1) 

@dataclass
class Rectangle:
    length: float
    width: float
    color: str = 'white'
rect1 = Rectangle(12,14)
rec2 = Rectangle(5,7,'blue')
print(rect1)
print(rec2.color)


@dataclass
class Point:
    x: int
    y: int

p = Point(3,4)
print(f"Point coordinates: ({p.x}, {p.y})")
p.x = 10
print(f"Updated Point coordinates: ({p.x}, {p.y})")


# Inheritance in Dataclass

@dataclass
class Person:
    name: str
    age: int

@dataclass
class Employee(Person):
    employee_id: str
    department: str

p = Person('Krish', 25)
employee = Employee("KRish", 25,'123','AI')
print(employee.name)

# Nested DataClass

@dataclass
class Address:
    street: str
    city: str
    zip_code: str

@dataclass
class Person:
    name: str
    age: str
    address: Address
address = Address('123 Main Street', 'Banglore', '12345')
person = Person("Krish", 25, address)

print(person.address.city)