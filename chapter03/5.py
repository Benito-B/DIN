def kmToMiles(kms: int) -> int:
    kmPerMile = 1.6
    return round(kms/kmPerMile,3)

print("Eso son",kmToMiles(int(input("Introduce kilometros: "))), "millas")
