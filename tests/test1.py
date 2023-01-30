from gear_transfer.gear_transfer import Transfer
from multiprocessing import Process


def f(tr: Transfer):
    tr.value.value = 10
    for i in range(10):
        tr.put(f'hello from {i}')

    print(f'elem0: {tr.get()}')
    print(f'elem1: {tr.get()}')
    print(f'elem2: {tr.get()}')
    print(f'elem3: {tr.get()}')
    print(f'read: {tr.read_position}')
    print(f'write: {tr.write_position}')


tr = Transfer(10, 1)

p = Process(target=f, args=(tr,))
p.start()
p.join()


