class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, marks):
        student = {"name": name, "marks": marks}
        self.students.append(student)

    def display(self):
        print("All students:")
        for s in self.students:
            print(s["name"], "-", s["marks"])

    def topper(self):
        top = max(self.students, key=lambda x: x["marks"])
        print("Topper:", top["name"], "-", top["marks"])

    def average(self):
        total = sum(s["marks"] for s in self.students)
        avg = total / len(self.students)
        print("Average marks:", avg)

    def get_failed_students(self):
        print("Failed students:")
        for s in self.students:
            if s["marks"] < 40:
                print(s["name"], "-", s["marks"])

    def sort_students(self):
        sorted_students = sorted(self.students, key=lambda x: x["marks"])
        print("Sorted Students:")
        for s in sorted_students:
            print(s["name"], "-", s["marks"])
    
    def __str__(self):
        return f"StudentManager with {len(self.students)} students"


# Using class
sm = StudentManager()


sm.add_student("Somya", 100)
sm.add_student("Rahul", 30)
sm.add_student("Aman", 80)

sm.display()
sm.topper()
sm.average()
sm.get_failed_students()
sm.sort_students()
print(sm)