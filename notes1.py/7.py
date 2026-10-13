class student:
    def details(self):
        self.name = int(input("Enter name:"))
        self.roll = int(input("Enter Roll:"))
        self.branch = int(input("Enter branch:"))
    def display(self):
        print("Student name",self.name)
        print("Student roll number:",self.roll)
        print("Student branch:",self.branch)
s1 = student()
s1.details()
kess1.display()
        