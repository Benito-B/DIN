S = [[], [], [], [], [], [], [], [], [], []]


def put(s: list, name: str) -> int:
    bucket = hashit(name)
    if not isin(s, name):
        s[bucket].append(name)
        return bucket
    return -1


def isin(s: list, name: str) -> bool:
    bucket = hashit(name)
    return name in s[bucket]


def hashit(name: str) -> int:
    bucket = 0
    for bucket in range(len(name)):
        bucket += ord(name[bucket])
    return bucket % 10


def getout(s: list, name: str) -> bool:
    bucket = hashit(name)
    if isin(s, name):
        s[bucket].remove(name)
        return True
    return False


if __name__ == "__main__":
    put(S, "Juan")
    put(S, "Sara")
    put(S, "Eustaquio")
    put(S, "Gervasio")
    put(S, "Saturnino")
    print(S)
    put(S, "Juanito")
    print(S)
    print(put(S, "Juan"))
    print(S)
    getout(S, "Juan")
    getout(S, "Saturnino")
    print(S)