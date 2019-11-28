class Country(object):

    def __init__(self, name: str, population: int, area):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other) -> bool:
        return self.area > other.area

    def population_density(self) -> float:
        return self.area / self.population

    def __str__(self) -> str:
        return self.name + " has a population of " + str(self.population) + " and is " \
               + str(self.area) + " square KM"

    def __repr__(self) -> str:
        return "{}('{}',{},{})".format(self.__class__.__name__, self.name, self.population, self.area)


if __name__ == "__main__":
    c1 = Country("Españita", 5000000, 2000)
    c2 = Country("Country smaller than spain", 1, 1999)
    print("Españita es la más grande:", c1.is_larger(c2))
    print("Densidad de población en españita: ", c1.population_density())
    print([c1])
