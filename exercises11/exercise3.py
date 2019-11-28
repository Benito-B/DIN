def mating_pairs(ffemales: list, fmales: list) -> set:
    ret = set()
    for i in range(len(ffemales)):
        ret.add((ffemales.pop(), fmales.pop()))
    return ret


if __name__ == "__main__":
    females = ["pepa", "josefa", "antonia", "segismunda"]
    males = ["vicente", "demetrio", "cual", "tal"]
    male_gerbils = [1, 2, 3, 4]
    female_gerbils = [5, 7, 8, 9]
    print(mating_pairs(females, males))
    print(mating_pairs(female_gerbils, male_gerbils))
