def intresting_of_students(dict):
    interest_of_students = []
    length_lastname = 0
    for key, value in dict.items():
        if value.get('interests') != None:
            for i_result in value['interests']:
                interest_of_students.append(i_result)
        if value.get('surname') != None:
            length_lastname += len(value['surname'])
    print(interest_of_students, length_lastname)

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

intresting_of_students(students)