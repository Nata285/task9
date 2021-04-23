class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.grades = {}


    def rate_ST(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        self.all_grades = []
        for grade in self.grades.values():
            self.all_grades.extend(grade)
            rating = sum(self.all_grades) / len(self.all_grades)

        return f'Имя: {self.name}'  '\n' f'Фамилия: {self.surname}' '\n' \
           f'Средняя оценка за домашнее задание: {round((rating),2)}' \
          '\n' f'Курсы с процессе изучения: {self.courses_in_progress}' '\n'\
          'Завершенные курсы: Введение в программирование'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        self.all_grades = []
        for grade in self.grades.values():
            self.all_grades.extend(grade)
            rating = sum(self.all_grades) / len(self.all_grades)
        return f'Имя: {self.name}'  '\n' f'Фамилия: {self.surname}' \
        '\n' f'Средняя оценка за лекции: {round((rating),2)}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return f'Имя: {self.name}'  '\n' f'Фамилия: {self.surname}'


first_student = Student('Ruoy', 'Eman')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['GIT']

second_student = Student('Mark', 'Buzov')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['GIT']

cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']
cool_Reviewer.courses_attached += ['GIT']

b_Reviewer = Reviewer('Nata', 'Kim')
b_Reviewer.courses_attached += ['Python']
b_Reviewer.courses_attached += ['GIT']

cool_Reviewer.rate_hw(first_student, 'Python', 10)
cool_Reviewer.rate_hw(first_student, 'GIT', 9)

cool_Reviewer.rate_hw(second_student, 'Python', 4)
cool_Reviewer.rate_hw(second_student, 'GIT', 7)

b_Reviewer.rate_hw(first_student, 'Python', 8)
b_Reviewer.rate_hw(first_student, 'GIT', 3)

b_Reviewer.rate_hw(second_student, 'GIT', 7)
b_Reviewer.rate_hw(second_student, 'Python', 7)

cool_Lecturer = Lecturer('Andrey', 'Petrov')
cool_Lecturer.courses_attached += ['Python']
cool_Lecturer.courses_attached += ['GIT']

m_Lecturer = Lecturer('Fedor', 'Ivanov')
m_Lecturer.courses_attached += ['Python']
m_Lecturer.courses_attached += ['GIT']

first_student.rate_ST(cool_Lecturer, 'Python', 7)
first_student.rate_ST(cool_Lecturer, 'GIT', 6)

first_student.rate_ST(m_Lecturer, 'Python', 3)
first_student.rate_ST(m_Lecturer, 'GIT', 7)

second_student.rate_ST(cool_Lecturer, 'Python', 5)
second_student.rate_ST(cool_Lecturer, 'GIT', 6)

second_student.rate_ST(m_Lecturer, 'Python', 4)
second_student.rate_ST(m_Lecturer, 'GIT', 10)

print(first_student.grades)
print(second_student.grades)
print(cool_Lecturer.grades)
print(m_Lecturer.grades)
print(cool_Reviewer)
print(cool_Lecturer)
print(first_student)
print(second_student)
print(m_Lecturer)

students = []
students.append(first_student.grades)
students.append(second_student.grades)
print(students)


