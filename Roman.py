# Pair programming - Emily driver, Mary Kate navigator
def intToRom(num):
    rom = ''
    while num>0:
        if num>=900:
            if num<1000:
                rom = rom + 'CM'
                num = num - 900
            else:
                rom = rom + 'M'
                num = num - 1000
        elif num>=400:
            if num<500:
                rom = rom + 'CD'
                num = num - 400
            else:
                rom = rom + 'D'
                num = num - 500
        elif num>=90:
            if num<100:
                rom = rom + 'XC'
                num = num - 90
            else:
                rom = rom + 'C'
                num =num - 100
        elif num>=40:
            if num<50:
                rom = rom + 'XL'
                num = num - 40
            else:
                rom = rom + 'L'
                num = num - 50
        elif num>=9:
            if num<10:
                rom = rom + 'IX'
                num = num - 9
            else:
                rom = rom + 'X'
                num =num - 10
        elif num>=4:
            if num<5:
                rom = rom + 'IV'
                num = num - 4
            else:
                rom = rom + 'V'
                num = num - 5
        else:
            rom = rom + 'I'
            num = num - 1
    return rom

print(intToRom(1994))

print(intToRom(58))

print(intToRom(3))

# Pair programming - Mary Kate driver, Emily navigator
def romToInt(rom):
    int = 0