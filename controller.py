import data_keeper 
import input_data
import output_data


def start():
    i=1
    while i==1:
        print('Введите номер команды:\n\
    1.Показать список учеников\n\
    2.Поиск ученика по фамилии\n\
    3.Добавление ученика в список\n\
    4.Удалить ученика из списка\n\
    5.Показать список мест в кабинете\n\
    6.Поиск места ученика в кабинете по фамилии\n\
    7.Запись списка учеников файл в student.json\n\
    8.Запись списка мест файл cab.json')
        com=input_data.get_com()
        if com==1:
            stroka=''
            print("{:>10}".format('Фамилия'),"{:>10}".format('Имя'),"{:>11}".
            format('Год рожд.'),"{:>10}".format('Успеваимость'))
            for key, value in data_keeper.dir.items():
                valueList=value.split()
                print("{:>10}".format(key),"{:>10}".format(valueList[0]),
                "{:>11}".format(valueList[1]),"{:>12}".format(valueList[2]))
        if com==2:
            family=input_data.for_search()
            data_keeper.search(family)        
        if com==3:
            family, name, birth, coment, class_num, cab_num,place_num = input_data.new_data()
            data_keeper.directory_add(family, name, birth, coment, class_num, cab_num,place_num)
        if com==4:
            family=input_data.for_delete()
            data_keeper.delete(family)
        
        if com==5:
            stroka=''
            print("{:>10}".format('Фамилия'),"{:>10}".format('Класс'),"{:>11}".
            format('Кабинет №'),"{:>10}".format('Место'))
            for key, value in data_keeper.cab.items():
                valueList=value.split()
                print("{:>10}".format(key),"{:>10}".format(valueList[0]),
                "{:>11}".format(valueList[1]),"{:>10}".format(valueList[2]))
        if com==6:
            family=input_data.for_search()
            data_keeper.search_cab(family)
        if com==7:
            output_data.rewrite_student (data_keeper.dir)
        if com==8:
            output_data.rewrite_cab (data_keeper.cab)
        
        
        
        
        i=int(input('Желаете продолжить? (1-да, 2-нет)'))           
