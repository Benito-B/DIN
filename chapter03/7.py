def averageGrades(grade1: int, grade2: int, grade3:int, grade4: int) -> int:
    gradeList = [grade1,grade2,grade3,grade4]
    gradeList.remove(min(gradeList))
    return (gradeList[0]+gradeList[1]+gradeList[2])/3
print("La media de las tres mejores notas es: ",
    averageGrades(int(input("Introduce la primera nota: ")),
    int(input("Introduce la segunda nota: ")),
    int(input("Introduce la tercera nota: ")),
    int(input("Introduce la cuarta nota: "))))
