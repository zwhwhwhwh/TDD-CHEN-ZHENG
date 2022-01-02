import math

def min_int(a,b):
    if a < b :
        return a
    else :
        return b


def mean_int(list):
    mean = sum(list)/len(list)
    return mean


def median_int(list):
    list.sort()
    l = len(list)
    if l%2==0:
        return (list[int(l/2)-1] + list[int(l/2)])/2
    else:
        return list[int(l/2)]


def ecart_int(list):
    mean = sum(list)/len(list)
    var = 0
    for i in list:
        var = var + (i-mean)**2
    var = var/len(list)
    ecart = round(math.sqrt(var),2)
    return ecart


def geometrique(list):
    c = list[1]/list[0]
    for i in range((len(list))-1):
        if (list[i+1]/list[i])!=c:
            return False
    return True


def arithmetique(list):
    c = list[1]-list[0]
    for i in range((len(list))-1):
        if (list[i+1]-list[i])!=c:
            return False
    return True


def is_geometrique(c, list):
    for i in range((len(list))-1):
        if (list[i+1]/list[i])!=c:
            return False
    return True


def is_arithmetique(c, list):
    for i in range((len(list))-1):
        if (list[i+1]-list[i])!=c:
            return False
    return True
