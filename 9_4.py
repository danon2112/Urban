from random import choice

# ====================== Lamda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda first_letter, second_letter: True if first_letter == second_letter else False, first, second))
print(result)

# ====================== Замыкание

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'a', encoding='utf8')
        for data in data_set:
            file.write(str(data) + '\n')

        file.close()

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# ====================== call

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())