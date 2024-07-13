from typing import Generator

#a generator is a type which avoids storing all values in memory, it just has a defined way of getting the next value if its in range
def generate(n: int) -> Generator[int, None, None]:
    '''
    Create specific generator for the given range.

    Parameters
    ----------
    n : int
        The range for the generator

    Returns
    -------
    Generator[int, None, None]
        A generator of 2*number+5 for numbers in range

    '''
    return (2*i+5 for i in range(n))

def main() -> None:
    gen = generate(10)
    print([i for i in gen], type(gen))

if __name__ == "__main__":
    main()