def tempconvert(var):
    try:
        return int(var)
    except ValueError , Argument:
        print("wrong argument passed",Argument)

tempconvert(2)
