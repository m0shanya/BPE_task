def swapping(number):
    """The function converts the number to the hex system in which I swap the bits and then
    translate back to the decimal system"""
    b = hex(number)
    print(b)
    b = f'0x{b[3]}{b[2]}'  # swapping bits
    print(f"Inverted number\t{b}")
    result = int(b, 16)
    print(result)


a = int(input("Input number(type int)\t"))
while a < 16 or a > 255:  # check for sign and number of bits
    a = int(input("Number should be more than 16 and less than 255.\nInput again(type int)\t"))
swapping(a)
