import json

def rewrite_student(dic,path = 'student.json'):
    with open(path, 'w',encoding='utf-8') as file:
        json.dump(dic, file, indent=2)
        file.close()

def rewrite_cab(dic,path = 'cab.json'):
    with open(path, 'w',encoding='utf-8') as file:
        json.dump(dic, file, indent=2)
        file.close()