def bytes_to_kilobytes(value):
    return value/1024
def kilobytes_to_bytes(value):
    return value *1024
if __name__=="__main__":
    num = float(input("Введите число: "))
    choice = input ("1 - байты в килобайты, 2 - килобайты в байты: ")
    if choice == "1":
        print (bytes_to_kilobytes(num))
    elif choice == "2":
        print (kilobytes_to_bytes(num))
    else:
        print("Неверный выбор")
            
