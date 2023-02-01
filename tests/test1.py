import random
import time
import ctypes
from pulse_package import PulsePackage

from gear_transfer.gear_transfer import Transfer
from multiprocessing import Process

class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def print(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')
        print(f'color: {self.color}')


cat1 = Cat('Mika', 4, 'orange')
cat1.print()
print()
package1 = PulsePackage()
package1.dump(cat1)
package1.print()
msg = package1.pkg_binary()
print(msg)

def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i].value, end=", ")

def f(tr: Transfer):
    # tr.put(bytes(f'hello from {random.randint(0, 10)}', "utf-8"))
    # tr.put(bytes(f'hello from {random.randint(0, 10)}', "utf-8"))
    # tr.put(bytes(f'hello from {random.randint(0, 10)}', "utf-8"))
    # tr.put(bytes(f'hello from {random.randint(0, 10)}', "utf-8"))
    # tr.put(bytes(f'hello from {random.randint(0, 10)}', "utf-8"))
    tr.put(msg)
    # tr.get()
    # tr.put(bytes(f'hello from {random.randint(0, 10)}', "utf-8"))
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



tr = Transfer(5, 1)

p = Process(target=f, args=(tr,))
p.start()
p.join()

msg2 = tr.get()
print(f'msg2: {msg2}')
package2 = PulsePackage()
package2.load(msg2)
package2.print()
cat2 = package2.data
print()
cat2.print()

# for i in range(7):
#     print(f'{i} : {tr.get()}')

print(tr.read_position)
print_arr(tr.array)
#
# time.sleep(2)
# p2 = Process(target=f2, args=(tr,))
# p2.start()
# p2.join()

# print()
# buffer_size = 100 * 10
# # a = ctypes.c_char * buffer_size
# a = ctypes.create_string_buffer(msg, buffer_size)
#
# print(f'a: {a.value}')
# print(f'a: {a.raw}')

