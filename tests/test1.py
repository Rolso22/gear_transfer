import random
import time
import ctypes

from gear_transfer.gear_transfer import Transfer
from multiprocessing import Process

def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i].value, end=", ")

def f(tr: Transfer):
    # tr.put(bytes(f'hello from {random.randint(0, 10)}', "utf-8"))
    # tr.put(bytes(f'hello from {random.randint(0, 10)}', "utf-8"))
    # tr.put(bytes(f'hello from {random.randint(0, 10)}', "utf-8"))
    # tr.put(bytes(f'hello from {random.randint(0, 10)}', "utf-8"))
    # tr.put(bytes(f'hello from {random.randint(0, 10)}', "utf-8"))
    tr.put(b'\x9f\xde\x82\x92\xb2AE\xa1\xbc\xcb\xaf\x9a\r\xeb;\xb2\x00e\x00e\xfb\x82\x94\xa1\x00\x00\x14\x00\x00N\x80\x04\x95\t\x00\x00\x00\x00\x00\x00\x00\x8c\x05empty\x94.\x80\x04\x95C\x00\x00\x00\x00\x00\x00\x00\x8c'
           b'\x08__main__\x94\x8c\x03Cat\x94\x93\x94)\x81\x94}\x94('
           b'\x8c\x04name\x94\x8c\x04Mika\x94\x8c\x03age\x94K\x04\x8c\x05color\x94\x8c\x06orange\x94ub.')
    print(f'read: {tr.read_position}')
    print(f'write: {tr.write_position}')
    print("f")
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


tr = Transfer(5, 100)

p = Process(target=f, args=(tr,))
p.start()
p.join()

for i in range(5):
    print(tr.array[i])

for i in range(7):
    print(f'{i} : {tr.get()}')

print(tr.read_position)
print_arr(tr.array)

time.sleep(2)
# p2 = Process(target=f2, args=(tr,))
# p2.start()
# p2.join()

arr = ctypes.c_char * 1024
data = b'\x9f\xde\x82\x92\xb2AE\xa1\xbc\xcb\xaf\x9a\r\xeb;\xb2\x00e\x00e\xfb\x82\x94\xa1\x00\x00\x14\x00\x00N\x80\x04\x95\t\x00\x00\x00\x00\x00\x00\x00\x8c\x05empty\x94.\x80\x04\x95C\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x03Cat\x94\x93\x94)\x81\x94}\x94(\x8c\x04name\x94\x8c\x04Mika\x94\x8c\x03age\x94K\x04\x8c\x05color\x94\x8c\x06orange\x94ub.'
arr = ctypes.create_string_buffer(data, 1024 * 100)
print(arr.value)

