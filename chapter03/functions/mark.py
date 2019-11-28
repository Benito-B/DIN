def getMark(mark: float) -> int:
    if mark < 5:
        print("Fail")
    elif mark <= 6:
        print("Good")
    elif mark <= 8:
        print("Quite good")
    else:
        print("Astonishing")

getMark(float(input("Introduce your exam result here: ")))
