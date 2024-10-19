def pot(a,b):
    l = int(1)
    p = a
    while (l < b):
        a = a*p
        l+=1
    resp = a
    return int(resp)
def num1():
    a = input("Digite o numero:")
    return int(a)
def num2():
    b = input("Digite a potência:")
    return int(b)
n1 = num1()
n2 = num2()
res = pot(n1,n2)
print(res)