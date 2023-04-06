class Students:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avrg = float()
        
    
    def rate_hw(self,lecturer,course,grade):
        if isinstance(lecturer, Lecturers) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        c_i_p = ",".join(self.courses_in_progress)
        f_c = ",".join(self.finished_courses)
        
        self.avrg = sum(sum(self.grades.values(),[])) / len((self.grades.values(),[]))
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avrg}\nКурсы в процессе изучения: {c_i_p}\nЗавершенные курсы: {f_c}'
        return res     
    
    def __lt__(self,other):
        if not isinstance(other,Students):
            print("No student")
            return
        return self.avrg < other.avrg

class Mentors:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturers(Mentors):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []
        self.avrg = float()

    def average(self):
        self.avrg = sum(sum(self.grades.values(),[]))/len(self.grades.values(),[])   

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avrg}'
        return res
    
    def __lt__(self,other):
        if not isinstance(other,Lecturers):
            print("No lecturer")
            return
        return self.avrg < other.avrg


class Reviewer(Mentors):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Students) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}' 
        return res


student_1 = Students('Svetlana', 'Hodchenkova', 'female')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['SQL']

student_2 = Students('Roman', 'Unusov', 'mail')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['SQL']

student_3 = Students('Tim', 'Rodd', 'mail')
student_3.courses_in_progress += ['SQL']
student_3.finished_courses += ['Java']



lecturer_1 = Lecturers('Ivan', 'Ivanov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturers('Petr', 'Petrov')
lecturer_2.courses_attached += ['Java']

lecturer_3 = Lecturers('Sidr', 'Sidorov')
lecturer_3.courses_attached += ['SQL']



reviewer_1 = Reviewer('Andjelina', 'Jolly')
reviewer_1.courses_attached += ['SQL']
reviewer_1.courses_attached += ['Java']
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Mikky', 'Mouse')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']
reviewer_2.courses_attached += ['SQL']



student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 10)

student_1.rate_hw(lecturer_2, 'Java', 5)
student_1.rate_hw(lecturer_2, 'Java', 7)
student_1.rate_hw(lecturer_2, 'Java', 8)

student_1.rate_hw(lecturer_3, 'SQL', 7)
student_1.rate_hw(lecturer_3, 'SQL', 8)
student_1.rate_hw(lecturer_3, 'SQL', 9)

student_2.rate_hw(lecturer_2, 'Java', 10)
student_2.rate_hw(lecturer_2, 'Java', 8)
student_2.rate_hw(lecturer_2, 'Java', 9)

student_3.rate_hw(lecturer_3, 'SQL', 5)
student_3.rate_hw(lecturer_3, 'SQL', 6)
student_3.rate_hw(lecturer_3, 'SQL', 7)




reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_2.rate_hw(student_2, 'Java', 9)

reviewer_2.rate_hw(student_3, 'SQL', 8)
reviewer_2.rate_hw(student_3, 'SQL', 7)
reviewer_2.rate_hw(student_3, 'SQL', 9)



print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}\n\n{lecturer_3}')
print()
print()

print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()


print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}')
print()


student_list = [student_1, student_2, student_3]
lecturer_list = [lecturer_1, lecturer_2, lecturer_3]

def student_rating(student_list, course_name):
    
    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.avrg
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


def lecturer_rating(lecturer_list, course_name):
    
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.avrg
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all



print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()


print(f"Средняя оценка для всех лекторов по курсу {'Java'}: {lecturer_rating(lecturer_list, 'Java')}")
print()
