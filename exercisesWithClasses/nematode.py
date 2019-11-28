class Nematode(object):

    def __init__(self, name: str, length: float, gender: str, age: int):
        self.name = name
        self.length = length
        self.gender = gender
        self.age = age

    def __str__(self):
        return "{} mide {} mm, es {} y tiene {} días".format(self.name, self.length, self.gender, self.age)

    def __repr__(self):
        return "{}({}, {}, {}, {})".format(self.__class__.__name__, self.name, self.length, self.gender, self.age)


if __name__ == "__main__":
    gusano1 = Nematode("Gusano enano", 0.9, "Hermafrodita", 2)
    print(gusano1)
    print([gusano1])
