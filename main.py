from pathlib import Path
import time
from contextlib import contextmanager
from itertools import chain

@contextmanager
def timer():
    start = time.time()
    yield
    finish = time.time()
    print(f'Executed in {finish-start:2}')


if __name__ == '__main__':
    pass
