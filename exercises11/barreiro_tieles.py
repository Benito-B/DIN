def cartProd(set1: set, set2: set) -> set:
    """
    Takes two sets and returns the cartesian product of them
    :param set1: First set
    :param set2: Seconds set
    :return: Set with cartesian product of the two arguments

    >>>x = {'a', 'b'}
    >>>y = {'c', 'd'}
    >>>print(cartProd(x, y))
    >>>{('b', 'c'), ('a', 'c'), ('b', 'd'), ('a', 'd')}
    """
    result = set()
    for elem in set1:
        for innerelem in set2:
            result.add((elem, innerelem))
    return result


def delDups(l: list) -> list:
    """
    Takes a list and returns a new one without duplicated values
    :param l: list with duplicated values
    :return: new list without duplicated values

    >>>x = [1, 2, 2, 3]
    >>>print(delDups(x))
    """
    return list(set(l))


def clearCode() -> dict:
    """
    Function that generates a dictionary with the all the lowercase letters in it but ñ
    :return: dictionary with almost all the spanish' language characters
    >>>print(clearCode())
    """
    d = dict()
    for letter in range(97, 123):
        d[chr(letter)] = chr(letter)
    return d


def shuffleDict(d: dict) -> dict:
    """
    Takes a dictionary and returns it after shuffling it's values
    :param d: Sorted dictionary
    :return: shuffled dictionary
    >>>print(shuffleDict(clearCode()))
    """
    import random
    keys = list(d.keys())
    new_d = dict()
    vals = list(d.values())
    random.shuffle(vals)
    for i in range(len(d)):
        new_d[keys[i]] = vals[i]
    return new_d


def encrypt(s: str, d: dict) -> str:
    """
    Function that takes a string and encrypts it.
    :param s: The string to encrypt
    :param d: Dictionary to use in the encryption
    :return: Encrypted string
    >>>print(encrypt("test", shuffleDict(clearCode())))
    """
    encrypted = ""
    for char in s:
        encrypted += d[char]
    return encrypted


def reverseDict(d: dict) -> dict:
    vals = list(d.values())
    keys = list(d.keys())
    new_d = dict()
    for i in range(len(vals)):
        new_d[vals[i]] = keys[i]
    return new_d


if __name__ == "__main__":
    s = input("Introduce contraseña a encriptar: ")
    d = shuffleDict(clearCode())
    print("La contraseña encriptada es:", encrypt(s, d))

    print("Random dictionary:", d)
    print("Reversed dictionary:", reverseDict(d))
