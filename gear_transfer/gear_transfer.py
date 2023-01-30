import ctypes
from multiprocessing import Array, Value


class Transfer:
    def __init__(self, buffer_count: int, buffer_size: int) -> None:
        self.read_position = 0
        self.write_position = 0
        self.buffer_count = buffer_count
        self.buffer_size = buffer_size * 1024  # Kb -> bytes
        self.array = Array(ctypes.c_char * self.buffer_size, buffer_count)
        for i in range(self.buffer_count):
            self.array[i] = ctypes.create_string_buffer(b'', self.buffer_size)

    def read_pos_inc(self):
        self.read_position += 1
        if self.read_position == self.buffer_count:
            self.read_position = 0

    def write_pos_inc(self):
        self.write_position += 1
        if self.write_position == self.buffer_count:
            self.write_position = 0

    def find(self):
        with self.array.get_lock():
            pos = self.read_position
            while self.read_position != pos:
                if self.read_position == self.buffer_count:
                    self.read_position = 0
                if self.array[self.read_position].value != b'':
                    return self.get_elem()
                else:
                    self.read_pos_inc()
            self.read_position = 0
            return None

    def get_elem(self):
        if self.array[self.read_position].value != b'':
            elem = self.array[self.read_position].value
            self.array[self.read_position].value = b''
            # print(f'get in {self.read_position} -> {self.read_position + 1}')
            self.read_pos_inc()
            return elem
        self.read_pos_inc()
        return None

    def get(self):
        elem = self.get_elem()
        if elem is None:
            return self.find()
        else:
            return elem

    def put_elem(self, data):
        if self.array[self.write_position].value == b'':
            # print(f'put in {self.write_position}')
            self.array[self.write_position] = ctypes.create_string_buffer(data, self.buffer_size)
            self.write_pos_inc()
            return True
        else:
            self.write_pos_inc()
            return False

    def put(self, data):
        with self.array.get_lock():
            if not self.put_elem(data):
                pos = self.write_position
                while self.write_position != pos:
                    if self.write_position == self.buffer_count:
                        self.write_position = 0
                    if self.array[self.write_position].value == b'':
                        self.put_elem(data)
                    else:
                        self.write_pos_inc()
                self.write_position = 0
                raise "no place"

