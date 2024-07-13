#if an exception is thrown somewhere between open and close, the file will never be closed
def manually_calling_close(filename):
    f = open(filename)
    print(f.read() + '\n')
    f.close()

#even if an exception is thrown, the file will still be closed
def using_with_statement(filename):
    with open(filename) as f:
        print(f.read() + '\n')

def main() -> None:
    FILENAME = "file_handling/file.txt"
    manually_calling_close(FILENAME)
    using_with_statement(FILENAME)

if __name__ == "__main__":
    main()

#this also pertains to other resources that need to be closed, its better to use with-as than try-finally