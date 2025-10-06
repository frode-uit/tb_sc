# file: sc_10_03_iterator.py
from collections.abc import Iterator

class MyIterator(Iterator):
    def __init__(self):
        self.data = [1, 2, 3]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

my_iterator = MyIterator()
for item in my_iterator:
    print(item)
