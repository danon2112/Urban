import multiprocessing
import time


def read_info(file_name):
    all_data = []
    with open(file_name, 'r', encoding='utf8') as file:
        for string in file.readlines():
            all_data.append(string)

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

t1 = time.time()
read_info(files[0])
read_info(files[1])
read_info(files[2])
read_info(files[3])
print('t1=', time.time() - t1)

t2 = time.time()
if __name__ == '__main__':
    mp1 = multiprocessing.Process(target=read_info, args=('file 1.txt', ))
    mp2 = multiprocessing.Process(target=read_info, args=('file 2.txt', ))
    mp3 = multiprocessing.Process(target=read_info, args=('file 3.txt', ))
    mp4 = multiprocessing.Process(target=read_info, args=('file 4.txt', ))
    mp1.start()
    mp2.start()
    mp3.start()
    mp4.start()


print('t2=', time.time() - t2)