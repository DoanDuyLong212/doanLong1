import math
    
a = float(input('nhap so a: '))
b = float(input('nhap so b: '))
c = float(input('nhap so c: '))
x = float(input('nhap so x: '))

def phuong_trinh_bac2(a,b,c,x):
    S1 = a*x*x + b*x + c
    print(S1)

def kiem_tra_delta(a,b,c,x):
    delta = b*b - 4*a*c
    if delta > 0:
        S2 = math.sqrt(delta)
    else:
        S2 = 0
    print(S2)
    
a = float(input('nhap lai so a: '))
b = float(input('nhap lai so b: '))
c = float(input('nhap lai so c: '))

def kiem_tra_tam_giac(a,b,c):
    if a + b > c and b + c > a and a + c > b:
        return 1
    return 0
if kiem_tra_tam_giac(a,b,c) == 1:
    print('are side of a triangle')
if kiem_tra_tam_giac(a,b,c) == 0:
    print('are not side of a triangle')

def tam_giac(check,a,b,c):
    if check:
        p = (a+b+c)/2
        S1 = math.sqrt(p*(p-a)*(p-b)*(p-c))
        p = (a + b + c) / 2
        print('area: ',S1,'perimeter: ',p)
    else:
        print("a, b, c are not side of a triangle")
        return 0
    
check = kiem_tra_tam_giac(a,b,c)
S1 = tam_giac(check,a,b,c)