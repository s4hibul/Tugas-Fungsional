def pangkat(a,b):
    if b>1:
        return a*pangkat(a,b-1)
    return a
print(pangkat(3,2))