print("To jest kalkulator dodawania, odejmowania, dzielenia i mnozenia")
a = float ( input ( ' podaj A : ') )
b = float ( input ( ' podaj B : ') )
operacja = input ( ' podaj operacje : ')

if operacja == '+':
    print ( f'{ a } + { b } = { a + b } ')
elif operacja == '-':
    print(f'{a} - {b} = {a-b}')
elif operacja == '*':
    print(f'{a} * { b } = {a * b}')
elif operacja == '/':
    if b == 0:
        print("nie dzielimy przez zero")
    else:
        print(f'{a} / { b } = {a / b}')
