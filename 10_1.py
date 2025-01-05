import time
import threading


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf8') as file:
        for string_num in range(word_count):
            file.write(f'Какое-то слово № {string_num}')
            time.sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')

t1 = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
print('Время работы потока', time.time() - t1)

t3 = time.time()
th1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
th2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
th3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
th4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
th1.start()
th2.start()
th3.start()
th4.start()
th1.join()
th2.join()
th3.join()
th4.join()
print('Время работы потока', time.time() - t3)