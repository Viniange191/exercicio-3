def Num():
    n=input("Digite um numero:")
    inver = " "
    for s in n:
        inver = s + inver
    return int(inver)
l = Num()
print(l)
