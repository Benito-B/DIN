def averageGrades(grade1: int, grade2: int, grade3: int) -> float:
    return round((grade1+grade2+grade3)/3,2)

print("La nota media de esas notas es",averageGrades(int(input("Introduce nota 1: ")),
    int(input("Introduce nota 2: ")),
    int(input("Introduce nota 3: "))))
