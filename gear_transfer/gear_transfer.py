import ctypes
from multiprocessing import Array, Value


class Transfer:
    def __init__(self, buffer_count: int, buffer_size: int) -> None:
        self.read_position = 0
        self.write_position = 0
        self.buffer_count = buffer_count
        self.buffer_size = buffer_size * 1024  # Kb -> bytes
        self.array = Array(ctypes.c_wchar * self.buffer_size, buffer_count)

    def find(self):
        with self.array.get_lock():
            while self.array[self.read_position].value == '':
                if self.read_position == self.buffer_count:
                    self.read_position = 0
                    return None
                self.read_position += 1
            print(f'get in {self.read_position}')
            elem = self.array[self.read_position].value
            self.array[self.read_position].value = ''
            self.read_position += 1
            return elem

    def get(self):
        return self.find()

    def put(self, data):
        with self.array.get_lock():
            while self.array[self.write_position].value != '':
                if self.write_position == self.buffer_count:
                    self.write_position = 0
                    raise "no place"
                self.write_position += 1

            print(f'put in {self.write_position}')
            self.array[self.write_position] = ctypes.create_unicode_buffer(data, self.buffer_size)
            self.write_position += 1


