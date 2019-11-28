from country import Country


class Continent(object):

    def __init__(self, name: str, countries: list):
        self.name = name
        self.countries = countries

    def total_population(self) -> int:
        totalpop = 0
        for country in self.countries:
            totalpop += country.population
        return totalpop

    def __str__(self) -> str:
        ret = self.name + ":\n"
        for country in self.countries:
            ret += "{}\n".format(country)
        return ret


if __name__ == "__main__":
    c1 = Country("Galicia", 1000, 5)
    c2 = Country("Valencia", 999, 3)
    c3 = Country("Madrid", 5, 100)
    continent = Continent("España no es un continente pero me vale", [c1, c2, c3])
    print("Total population: ", continent.total_population())
    print(continent.name)
    print("\nPrinting continent:\n\n", continent)
