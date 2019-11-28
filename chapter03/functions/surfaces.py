def surface(option: int = -1, width: float = -1, height: float = -1, radius: float = -1) -> float:
    """ Calculates the surface of the specified figure with the given parameters:
        option: choosen figure (Square -> 1, Triangle -> 2, Circle -> 3)
        width: width of the base of the choosen figure
        height: height of the choosen figure
        radius: radius of the given figure (circle only)
    """
    from math import pi
    #If the module it's called directly, print the menu and let the user choose an option
    if __name__ == "__main__":
        print("Menu\n")
        print("\t1.- Square\n")
        print("\t2.- Triangle\n")
        print("\t3.- Circle\n")
        option = int(input("Choose the figure which's area you want to calculate: "))

    if option == 1:
        if __name__ == "__main__":
            width = float(input("Introduce the square's base: "))
        return print("The area of the square is",width*width)
    elif option == 2:
        if __name__ == "__main__":
            width = float(input("Introduce the triangle's base: "))
            height = float(input("Introduce the triangle's height: "))
        return print("The area of the triangle is", width*height/2)
    elif option == 3:
        if __name__ == "__main__":
            radius = float(input("Introduce the circle's radius: "))
        return print("The area of the circle is ", pi*(radius*radius))
    else:
        print("That's not a valid option.")

if __name__ == "__main__":
    surface()
