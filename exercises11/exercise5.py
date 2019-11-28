def count_unique(d: dict) -> int:
    return len(set(d.values()))


if __name__ == "__main__":
    di = {'red': 1, 'green': 1, 'blue': 2, 'black': 3}
    print(count_unique(di))
