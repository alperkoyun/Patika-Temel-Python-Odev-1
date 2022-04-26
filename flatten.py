flatten = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
liste = []

def cevir(flatten):
    for i in flatten:
        if type(i) == list: 
            cevir(i)
        else: 
            liste.append(i)
    return liste
