import math

a = float(input("Qual o valor de A? "))
b = float(input("Qual o valor de B? "))
c = float(input("Qual o valor de C? "))

delta = b**2 - 4*a*c

if delta<0:
    print ("Não existem raízes reais")
else:
    if delta == 0:
        ru = -b / (2*a)
        print ("A única raiz é:",ru)
    else:
        r1 = -b + sqrt(delta) / (2*a)
        r2 = -b - sqrt(delta) / (2*a)
        print ("As raízes reais são", r1, "e",r2)

