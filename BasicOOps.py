class Students:
    def __init__(self,name,email,rollNo,marks):
        self.name=name
        self.email=email
        self.rollNo=rollNo
        self.marks=marks

    def student_details(self):
        print(f'Name:{self.name}')
        print(f'Email:{self.email}')
        print(f'Roll No:{self.rollNo}')
        print(f'Marks:{self.marks}')

s1=Students('Darshan','darshan@gmail.com',101,56)
s2=Students('Pradhumna','pradhumna@gmail.com',420,10)

s1.student_details()
s2.student_details()
