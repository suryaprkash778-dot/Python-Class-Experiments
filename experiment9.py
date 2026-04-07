#1.Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 objects by taking inputs from the user and display details of all students.
class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks  # dictionary with subjects

    def display(self):
        print(f"Name: {self.name}")
        print(f"SAP ID: {self.sap_id}")
        print(f"Marks: Physics={self.marks['phy']}, Chemistry={self.marks['chem']}, Maths={self.marks['maths']}")
        print("-" * 40)


# Create 3 student objects by taking input from the user
students = []
for i in range(3):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy = int(input("Enter Physics marks: "))
    chem = int(input("Enter Chemistry marks: "))
    maths = int(input("Enter Maths marks: "))
    
    marks = {'phy': phy, 'chem': chem, 'maths': maths}
    student = Student(name, sap_id, marks)
    students.append(student)

# Display details of all students
print("\n--- Student Details ---")
for s in students:
    s.display()

#2. Add constructor in the above class to initialize student details of n students and implement following methods:
#a)	Display() student details
#b)	Find Marks_percentage() of each student
#c)	 Display result() [Note: if marks in each subject >40% than Pass else Fail]
#d)	Write a Function to find average of the class.
class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.marks = {'phy': phy, 'chem': chem, 'maths': maths}

    def display(self):
        print(f"Name: {self.name}")
        print(f"SAP ID: {self.sap_id}")
        print(f"Marks: Physics={self.marks['phy']}, Chemistry={self.marks['chem']}, Maths={self.marks['maths']}")
        print("-" * 40)

    def marks_percentage(self):
        total = sum(self.marks.values())
        percentage = (total / 300) * 100   # each subject out of 100
        return percentage

    def result(self):
        # Pass if each subject > 40%
        if all(mark >= 40 for mark in self.marks.values()):
            return "Pass"
        else:
            return "Fail"


# Function to compute class average
def class_average(students):
    total_scores = sum(sum(s.marks.values()) for s in students)
    avg = total_scores / (len(students) * 3)   # 3 subjects per student
    return avg


# --- Main Program ---
students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy = int(input("Enter Physics marks: "))
    chem = int(input("Enter Chemistry marks: "))
    maths = int(input("Enter Maths marks: "))
    
    student = Student(name, sap_id, phy, chem, maths)
    students.append(student)

# Display details and results
print("\n--- Student Details and Results ---")
for s in students:
    s.display()
    print(f"Percentage: {s.marks_percentage():.2f}%")
    print(f"Result: {s.result()}")
    print("=" * 40)

# Display class average
print(f"\nClass Average Marks: {class_average(students):.2f}")

#3. Create programs to implement different types of inheritances.
# 1. Single Inheritance
class Parent:
    def show_parent(self):
        print("This is the Parent class.")

class Child(Parent):   # Single Inheritance
    def show_child(self):
        print("This is the Child class.")


# 2. Multiple Inheritance
class Father:
    def skill_father(self):
        print("Father: Driving")

class Mother:
    def skill_mother(self):
        print("Mother: Cooking")

class ChildMultiple(Father, Mother):   # Multiple Inheritance
    def skill_child(self):
        print("Child: Coding")


# 3. Multilevel Inheritance
class Grandparent:
    def show_gp(self):
        print("This is the Grandparent class.")

class ParentLevel(Grandparent):
    def show_parent(self):
        print("This is the Parent class (multilevel).")

class ChildLevel(ParentLevel):   # Multilevel Inheritance
    def show_child(self):
        print("This is the Child class (multilevel).")


# 4. Hierarchical Inheritance
class CommonParent:
    def common(self):
        print("Common Parent class")

class Child1(CommonParent):   # Hierarchical Inheritance
    def feature1(self):
        print("Child1 feature")

class Child2(CommonParent):   # Hierarchical Inheritance
    def feature2(self):
        print("Child2 feature")


# 5. Hybrid Inheritance (combination)
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

class D(B, C):   # Hybrid Inheritance
    def showD(self):
        print("Class D")


# --- Demonstration ---
print("\n--- Single Inheritance ---")
s = Child()
s.show_parent()
s.show_child()

print("\n--- Multiple Inheritance ---")
m = ChildMultiple()
m.skill_father()
m.skill_mother()
m.skill_child()

print("\n--- Multilevel Inheritance ---")
ml = ChildLevel()
ml.show_gp()
ml.show_parent()
ml.show_child()

print("\n--- Hierarchical Inheritance ---")
c1 = Child1()
c2 = Child2()
c1.common()
c1.feature1()
c2.common()
c2.feature2()

print("\n--- Hybrid Inheritance ---")
d = D()
d.showA()
d.showB()
d.showC()
d.showD()

#4. Create a class to implement method Overriding.
# Base class
class Animal:
    def sound(self):
        print("Animals make different sounds.")

# Derived class overriding the method
class Dog(Animal):
    def sound(self):   # Overriding the parent method
        print("Dog barks: Woof Woof!")

class Cat(Animal):
    def sound(self):   # Overriding the parent method
        print("Cat meows: Meow Meow!")

# Demonstration
print("--- Method Overriding Example ---")
a = Animal()
a.sound()   # Calls Animal's method

d = Dog()
d.sound()   # Calls Dog's overridden method

c = Cat()
c.sound()   # Calls Cat's overridden method
#5.Create a class for operator overloading which adds two Point Objects where Point has x & y values
#e.g. if
#P1(x=10,y=20)
#P2(x=12,y=15)
#P3=P1+P2 => P3(x=22,y=35)
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Operator overloading for +
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"


# Example usage
P1 = Point(10, 20)
P2 = Point(12, 15)

P3 = P1 + P2   # Calls __add__

print("P1:", P1)
print("P2:", P2)
print("P3 = P1 + P2:", P3)







