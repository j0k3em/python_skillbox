class Student:
    def __init__(self, name, num, perfomance):
        self.name = name
        self.num = num
        self.perfomance = perfomance

    def average_score(self):
        return sum(self.perfomance) / len(self.perfomance)

class Student_list:

    def __init__(self):
        self.students = []
        with open("students.txt", encoding = "UTF-8") as students_file:
            students_file = students_file.readlines()
            for line in students_file:
                stud_list = line.split()
                self.students.append(Student(stud_list[0] + " " + stud_list[1], stud_list[2], list(int(stud_list[i]) for i in range(3, 8))))

    def print_students(self):
        for i in self.students:
            print(i.name, round(i.average_score(), 1))

    def sort_students(self):
        self.students.sort(key=sort_key, reverse=True)

def sort_key(a):
    return a.average_score()

new_students = Student_list()
new_students.sort_students()
new_students.print_students()