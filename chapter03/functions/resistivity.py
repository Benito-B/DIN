def resistivity(r:float, a: float, l:float) -> float:
    """Calculates the resistivity of a piece of material given the following parameters:
    r -> Resistance of the material
    a: Area of the cross-sectional area of the specimen
    l: Lenght of the specimen
    
    If any of the parameters are invalid, the function returns -1

    Preconditions:
    r must be a positive number greater than zero.
    a must be a postive number greater than zero.
    l must be a positive number greater than zero.

    Usage:
    >>> resistivity(1,2,3)
    0.67

    >>> resistivity(7,15,20)
    5.25
    
    >>> resistivity(-1,6,-20)
    -1
    """
    if r <= 0 or a <= 0 or l <= 0:
        return -1
        
    return(round(r*(a/l),2))

