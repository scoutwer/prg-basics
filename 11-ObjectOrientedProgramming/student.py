# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.course = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.course = "IT"
    student2.name = "Olivia"
    student2.age = 21
    student2.course = "marketing"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, {student1.course}')
    print(f'{student2.name}, {student2.age} years old, {student2.course}')

if __name__ == "__main__":
    main()