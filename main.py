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
    # with timer():
    #     dpus = fsf.get_duplicates("C:\\Users\\AlistairKellaway\\git")

    # fsf.create_test_directory(4, "test_direc")
    r = fsf.get_duplicates("test_direc")
    for res in r.items():
        print(res)
        print()



    # print(dpus)
    # print(dpus2)