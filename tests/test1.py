import random
import time

from gear_transfer.gear_transfer import Transfer
from multiprocessing import Process

def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i].value, end=", ")

def f(tr: Transfer):
    tr.put({random.randint(0, 10)})
    tr.put({random.randint(0, 10)})
    tr.put({random.randint(0, 10)})
    tr.put({random.randint(0, 10)})
    tr.put({random.randint(0, 10)})
    print(f'read: {tr.read_position}')
    print(f'write: {tr.write_position}')
    print_arr(tr.array)
    print()


# def f2(tr: Transfer):
#     while (True):
#         tr.get()
#         tr.get()
#         print(f'read: {tr.read_position}')
#         print(f'write: {tr.write_position}')
#         print_arr(tr.array)
#         print()
#         time.sleep(3)


tr = Transfer(5, 1)

p = Process(target=f, args=(tr,))
p.start()
p.join()

for i in range(5):
    print(tr.array[i].value)

for i in range(7):
    print(f'{i} : {tr.get()}')

print(tr.read_position)
print_arr(tr.array)

time.sleep(2)
# p2 = Process(target=f2, args=(tr,))
# p2.start()
# p2.join()


