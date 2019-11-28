def find_dups(l: list) -> set:
    ret = set()
    for element in l:
        if l.count(element) > 1:
            ret.add(element)
    return ret


if __name__ == "__main__":
    lista = list()
    lista.append(2)
    lista.append(2)
    lista.append(3)
    lista.append(4)
    lista.append(4)
    lista.append(5)
    lista.append(7)
    print(find_dups(lista))
