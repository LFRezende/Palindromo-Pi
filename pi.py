def Pi(arq):
    arc = open(arq, "rt")  # Reads the Pi.txt document (contains 1 million digits)
    strnum = arc.read()  # Passes to string
    listnum = strnum.split()  # Splits to list, to get rid of the spaces
    strnum = "".join(listnum)  # Rejoins it as a string
    return strnum
