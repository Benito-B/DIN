def calculate(a: int = 2, b: int = 3, c:int = 1) -> int:
    """Precondition: all three values must be positive
    Does some weird math
    with the given numbers
    >>> calculate(1,20,1)
    Los resultados son -0.05012562893380057 y -19.9498743710662

    >>> calculate()
    Los resultados son -0.5 y -1.0
    """
    pos = (-b + (b**2-4*a*c)**0.5)/(2*a)
    neg = (-b - (b**2-4*a*c)**0.5)/(2*a)
    print("Los resultados son",pos, "y", neg)
