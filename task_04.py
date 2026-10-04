def swap(a, b):
    a = a+b
    b=a-b
    a=a-b
    return a, b
if  __name__=="__main__":
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"До обмена: a = {a}, b = {b}")
    a,b = swap(a, b)
    print(f"После обмена:  a = {a}, b = {b}")
