a = int(input("Input number(type int)\t"))  # ввод целого числа
while a < 16 or a > 255:  # проверка на знак и количество битов
    a = int(input("Number should be more than 16 and less than 255.\nInput again(type int)\t"))
b = hex(a)  # перевод в шестнадцатиричную систему
print(b)
b = f'0x{b[3]}{b[2]}'  # меняю местами биты
print(f"Inverted number\t{b}")
result = int(b, 16)  # перевожу в десятичную систему
print(result)
