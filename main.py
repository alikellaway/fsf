import time
from contextlib import contextmanager
import fsf


@contextmanager
def timer():
    start = time.time()
    yield
    finish = time.time()
    print(f'Executed in {finish-start:2}')


if __name__ == '__main__':
    with timer():
        fsf.get_duplicatea