#The use of d.keys() in for key in d.keys() is redundant
#The default way of iterating through dictionaries is through keys
def forKeyInDictKeys(d: dict) -> None:
    for key in d.keys():
        print(key, d[key])
    print()

#This is better
def forKeyInDict(d: dict) -> None:
    for key in d:
        print(key, d[key])
    print()

#This method works on a copy of the keys from a dictionary
#Usefull when modifying the dictionary
def forKeyInDictCopyOfKeys(d: dict):
    for key in list(d):
        print(key, d[key])
    print()

#Looping through the keys of a dictionary as well as the corresponding values
def dict_items(d: dict):
    for key, val in d.items():
        print(key, val)
    print()

def main() -> None:
    ages = {"Bob" : 34, "Anne" : 71, "Elizabeth" : 6, "Jarvis" : 25}
    #Both functions produce the same output
    forKeyInDictKeys(ages)
    forKeyInDict(ages)

    forKeyInDictCopyOfKeys(ages)

    dict_items(ages)

if __name__ == "__main__":
    main()