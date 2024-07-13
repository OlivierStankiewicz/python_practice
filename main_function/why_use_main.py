#checking if __name__ == '__main__' prevents code from imported files unintentionally running (see example_library.py for refference)
import example_library
from time import perf_counter

def main(iterations: int) -> int:
    #time.perf_counter() is more accurate than time.time() for timing code execution
    start = perf_counter()
    for i in range(iterations):
        pass
    time = perf_counter() - start
    return time
    
if __name__ == '__main__':
    #using a main function leads to faster code execution
    ITERATIONS = 1_000_000

    time_function = main(ITERATIONS)
    print(f'\nTime it took using main function: {time_function}')

    start_globally = perf_counter()
    for i in range(ITERATIONS):
        pass
    time_globally = perf_counter() - start_globally
    print(f'Time it took globally: {time_globally}')

    #not using main leads to variables being left in scope unintentionally
    for i in range(10):
        pass
    print(f'\nValue of i outside of the for loop it was used in : {i}')