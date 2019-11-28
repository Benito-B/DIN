class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def __str__(self) -> str:
        return self.name + " sabe: " + str(self.tricks)


d1 = Dog('Perrito')
d2 = Dog('Perrete')

d1.add_trick("Dar la pata")

print(d1, d2)
