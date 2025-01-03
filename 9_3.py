from sys import intern

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(value[0]) - len(value[1]) for value in list(zip(first, second)) if len(value[0]) != len(value[1]))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))

