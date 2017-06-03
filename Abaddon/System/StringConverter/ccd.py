def argsconnect(argsin, argsou):

    argstocheck = argsin
    argstorelat = argsou

    atclength   = len(argstocheck)
    atrlength   = len(argstorelat)

    gendict = {}

    for num in range(0, atclength):

        gendict[str(argstocheck[num])] = str(argstorelat[num])


    return gendict
