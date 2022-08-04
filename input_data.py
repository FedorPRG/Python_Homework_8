def get_com():
    i=0
    while i==0:
        com=int(input('?: '))
        if com<1 or com>9:
            print('Вы ввели не правильное значение\n\
Введите номер команды')
        else: i=1
    return com
def new_data():
    family=str(input('Введите фамилию: '))
    name=str(input('Введите имя: '))
    birth=str(input('год рождения: '))
    coment=str(input('Введите комментарий: '))
    class_num=str(input('Введите номер класса: '))
    cab_num=str(input('Введите номер кабинета: '))
    place_num=str(input('Введите номер места в кабинете: '))
    return  family,name, birth, coment, class_num, cab_num,place_num
def for_search():
    family=str(input('Введите фамилию для поиска: '))
    return family
def for_delete():
    family=str(input('Введите фамилию для удаления: '))
    return family
# def output_format():
#     i=0
#     while i==0:
#         format=int(input('Выберите формат вывода 1 или 2: '))
#         if format<1 or format>2:
#             print('Вы ввели не правильное значение')
#         else: i=1
#     return format