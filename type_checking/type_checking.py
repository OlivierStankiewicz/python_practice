from collections import namedtuple

#checks if the variable is literally of type t
def chcecking_type_equality(var: any, t: type) -> bool:
    return type(var) == t

#checks if the variable is an instance of type t, meaning it can be of a type which can be a subclass of t
def chcecking_isinstance(var: any, t: type) -> bool:
    return isinstance(var, t)

def main() -> None:
    some_tuple = (1, 2, 3)
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)

    print('Checking if a simple tuple variable is equal to a tuple type')
    print(chcecking_type_equality(some_tuple, tuple))

    print('Checking if a named tuple variable is equal to a tuple type')
    print(chcecking_type_equality(p, tuple))

    print('Checking if a simple tuple variable is an instance of tuple type')
    print(chcecking_isinstance(some_tuple, tuple))

    print('Checking if a named tuple variable is an instance of tuple type')
    print(chcecking_isinstance(p, tuple)) 

if __name__ == "__main__":
    main()