#import pandas as pd
import json

def read_student(path = 'student.json'):
    with open(path, 'r',encoding='utf-8') as file:
        data = json.load(file)
        file.close()
    return data

def read_cab(path = 'cab.json'):
    with open(path, 'r',encoding='utf-8') as file:
        data = json.load(file)
        file.close()
    return data


cab= read_cab()

dir = read_student()

def directory_add(family,name,birth,coment, class_num, cab_num,place_num):
    dir[family]=f'{name}      {birth}  {coment}'
    cab[family]=f'{class_num} {cab_num} {place_num}'

def search(family):
    for key, value in dir.items():
        if key==family:
            print("{:>10}".format('Фамилия'),"{:>10}".format('Имя'),"{:>11}".
            format('Год рожд.'),"{:>10}".format('Успеваимость'))
            valueList=value.split()
            return print("{:>10}".format(key),"{:>10}".format(valueList[0]),
                "{:>11}".format(valueList[1]),"{:>12}".format(valueList[2]))
def search_cab(family):
    for key, value in cab.items():
        if key==family:

            print("{:>10}".format('Фамилия'),"{:>10}".format('Класс'),"{:>11}".
            format('Кабинет №'),"{:>10}".format('Место'))
            valueList=value.split()
            return print("{:>10}".format(key),"{:>10}".format(valueList[0]),
                "{:>11}".format(valueList[1]),"{:>10}".format(valueList[2]))
    else: print(f'Записи с фамилией {family} нет')

def delete(family):
    for key, value in list(dir.items()):
        if key==family:
            del dir[family]
            print('Фамилия удалена')
            break
    print(f'Записи с фамилией {family} нет')    