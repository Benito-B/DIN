def fetch_authors(file: str) -> list:
    authors = list()
    f = open(file, 'r')
    fl = f.readlines()
    f.close()
    for line in fl:
        i = line.lower().find("author")
        if i >= 0:
            authors.append(line[i+6:].strip())
    return authors


if __name__ == "__main__":
    print(fetch_authors("molecules.txt"))

