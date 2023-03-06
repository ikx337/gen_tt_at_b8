def conv(a, base):
    result = []
    if(a == 0):
        result.append(0)
    else:
        # Calcul of pounds
        nbOfDigits = 0
        pounds = []
        while(a >= base**nbOfDigits):
            pounds.append(base**nbOfDigits)
            nbOfDigits += 1
        pounds.reverse()

        # Conversion
        for i in range(len(pounds)):
            result.append(divmod(a, pounds[i])[0])
            a = divmod(a, pounds[i])[1]
    return(result)

def onNdigit(a, nbOfDigits):
    for i in range(1, nbOfDigits):
        while(len(a) < nbOfDigits):
            a.insert(i-1,0)
    return(a)
