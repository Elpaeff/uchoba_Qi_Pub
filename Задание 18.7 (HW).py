import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Редактировать оценки по предмету у ученика
        5. Добавить ученика
        6. Удалить ученика
        7. Добавить предмет ученику
        8. Удалить предмет у ученика
        9. Вывести все оценки у ученика
        10. Вывести средний бал по предмету у ученика
        11. Вывести список Учеников
        12. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')

        student = input('Введите имя ученика: ')

        class_ = input('Введите предмет: ')

        mark = int(input('Введите оценку: '))

        if student in students_marks.keys() and class_ in students_marks[student].keys():

            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')

        for student in students:
            print(student)
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')

        for student in students:
            print(student)

            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
    elif command == 4:
        print("Изменить оценки у ученика")
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            for class_ in classes:

             print(f'{class_} - {students_marks[student][class_]}')
            class_ = input('Введите предмет: ')
            if class_ in students_marks[student].keys():
                    mark_nbr = int(input('Введите порядковый номер оценки: ')) - 1 #порядковый номер оценки
                    mark = int(input('Введите оценку: '))
                    students_marks[student][class_].pop(mark_nbr)
                    students_marks[student][class_].insert(mark_nbr, mark)
                    print(f'Для {student} по предмету {class_} оценка в ячейке {mark_nbr + 1}  изменена на оценку - {mark}')
            else: print("данного предмета нет в базе" )

        else: print("Ученик отсутствует в базе")
    elif command == 5:
        print("Добавление нового ученика")
        student = input('Введите имя нового ученика: ')
        if student in students:
            print("Данный ученик уже есть в списке учеников")
        else:
            students.append(student)
            students_marks[student] = {}
            for class_ in classes:
                marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
                students_marks[student][class_] = marks
            print(f'{student} добавлен в список учеников')
    elif command == 6:
        print("Удаление ученика")
        student = input("Введите имя ученика:")
        if student in students:
            students.remove(student)
            students_marks.pop(student)
            print(f'{student} - Удален из базы данных')
        else: print("данный ученик отсутствует в базе данных")
    elif command ==7:
        print("Добавить предмет ученику")
        student = input("Введите имя ученика:")
        if student in students_marks.keys():
            class_ = input("Введите название нового предмета: ")
            if class_ in students_marks[student].keys():
                print("Данный предмет уже есть в списке прдеметов")
            else:
                classes.append(class_)
                for class_ in classes:  # 1 итерация: class_ = 'Математика'
                    marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
                    students_marks[student][class_] = marks
                print(F'{class_}  добавлен в список предметов ')
                print(classes )
        else: print("Данного ученика нет в базе")
    elif command == 8:
        print("Удалить  предмет  у ученика")
        student = input("Введите имя ученика:")
        if student in students_marks.keys():
            class_ = input("Введите название нового предмета: ")
            if class_ in students_marks[student].keys():
                classes.remove(class_)
                print(F'Предмет "{class_}" - удален из списка прдеметов {student}')
            else:
                print("Данного предмета  нет в списке прдеметов")
        else:
            print("Данного ученика нет в базе")
    elif command == 9:
            print('9. Вывести все оценки у ученика')
            student = input('Введите имя ученика: ')
            if student in students_marks.keys():
             for class_ in classes:
                    print(f'{class_} - {students_marks[student][class_]}')
            else: print("Ученик отсутствует в базе")
            print()
    elif command == 10:
        print("Вывести средний бал по предмету у ученика")
        student = input("Введите имя ученика:")
        if student in students_marks.keys():
            class_ = input("Введите название предмета: ")
            if class_ in students_marks[student].keys():
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'средний бал по предмету "{class_}" - {marks_sum // marks_count}')
            else:
                print("Данного предмета нет в списке предметов")
        else:
                print("данного ученика не в базе учеников")
    elif command == 11:
        for student in students:
            print(student)
    elif command == 12:
        print('10. Выход из программы')
        break