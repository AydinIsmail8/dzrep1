class Mentor():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя:{self.name}\nФамилия:{self.surname}'




class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] #Этот атрибут представляет собой список курсов, к которым привязан данный наставник.
        self.grades = {}

    def rate_check(self, student):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'

        def __str__(self):
            return f'Имя:{self.name}\nФамилия:{self.surname}\n Средняя оценка за лекции: {self.grades}'

        def __str__(self):
            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade()}"

        def __lt__(self, other):
            return self.get_average_grade() < other.get_average_grade()

        def __le__(self, other):
            return self.get_average_grade() <= other.get_average_grade()

        def __eq__(self, other):
            return self.get_average_grade() == other.get_average_grade()

        def __ne__(self, other):
            return self.get_average_grade() != other.get_average_grade()

        def __gt__(self, other):
            return self.get_average_grade() > other.get_average_grade()

        def __ge__(self, other):
            return self.get_average_grade() >= other.get_average_grade()

        def get_average_grade(self):
            return sum(self.grades) / len(self.grades)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.rate_lecture(self, course, grade)
            else:
                return 'Ошибка'

    def __str__(self):
        return f'Имя:{self.name}\nФамилия:{self.surname}\n Средняя оценка за лекции: {self.grades}\n Курсы в процессе изучения: {self.courses_in_progress}\n Завершенные курсы: {self.finished_courses}'

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        return self.get_average_grade() >= other.get_average_grade()

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)




