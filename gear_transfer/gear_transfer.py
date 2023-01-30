import ctypes
from multiprocessing import Process, Array, Value


class Transfer:
    def __init__(self, buffer_count: int, buffer_size: int) -> None:
        self.read_position = 0
        self.write_position = 0
        self.buffer_count = buffer_count
        self.buffer_size = buffer_size * 1024  # Kb -> bytes
        self.array = Array(ctypes.c_wchar * self.buffer_size, buffer_count)
        self.value = Value('i', 0)

    def find(self):
        while self.array[self.read_position].value == '':
            if self.read_position == self.buffer_count:
                self.read_position = 0
                return None
            self.read_position += 1
        elem = self.array[self.read_position].value
        self.array[self.read_position].value = ''
        self.read_position += 1
        return elem

    def get(self):
        return self.find()

    def put(self, data):
        while self.array[self.write_position].value != '':
            if self.write_position == self.buffer_count:
                self.write_position = 0
                raise "no place"
            self.write_position += 1

        self.array[self.write_position] = ctypes.create_unicode_buffer(data, self.buffer_size)


