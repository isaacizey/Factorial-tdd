
def factorial(x):
    """Calculate the factorial of a number."""
    if x.__class__ == int:
        if x == 0:
            return 1
        

        elif x < 0 :
            return 0
        elif x < 1 and x > 0:
            return 1 
        else:
            return x * factorial(x-1)
    elif x.__class__ != int:
            return 0        

    else :
        return 0


    

