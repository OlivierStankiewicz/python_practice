def indexAndValue(l: list) -> None:
    for index, value in enumerate(l):
        print(index, value)

def synchronizedIteration(l1: list, l2: list):
    for v1, v2 in zip(l1, l2):
        print(f'{v1} - {v2}')
    
def synchronizedIterationWithIndexes(l1: list, l2: list):
    for index, (v1, v2) in enumerate(zip(l1, l2)):
        print(f'{index}. {v1} - {v2}')

def main() -> None:
    names = ["George", "John", "Peter", "Bob", "Thomas"]
    grades = [5, 3, 5, 1, 2]
    indexAndValue(names)
    print()
    synchronizedIteration(names, grades)
    print()
    synchronizedIterationWithIndexes(names, grades)

if __name__ == "__main__":
    main()