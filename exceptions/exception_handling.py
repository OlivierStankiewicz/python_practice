#this also catches keyboard interrupts or system exits
def bare_except():
    try:
        _ = int(input('Input a number: '))
    except:
        print('NaN')

#this will ignore the keyboard interrupts and system exits but is not clean
def capital_exeption():
    try:
        _ = int(input('Input a number: '))
    except Exception:
        print('NaN')

#this will handle the exeptions most approperietly
def valError_except():
    try:
        _ = int(input('Input a number: '))
    except ValueError:
        print('NaN')

def main() -> None:
    print('Bare except')
    bare_except()

    print('Capital Except exception')
    capital_exeption()

    print('ValueError exception')
    valError_except()

if __name__ == "__main__":
    main()