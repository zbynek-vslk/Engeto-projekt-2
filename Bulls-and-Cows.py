import random


def oddelovac() -> None:
    print('_'*len('Vygeneroval jsem čtyřmístné číslo'))


def hlavicka() -> None:
    print('Ahoj!')
    oddelovac()
    print('Vygeneroval jsem čtyřmístné číslo')
    print('Zahrajme si Bulls and Cows')
    oddelovac()
    print('Zadej číslo:')
    oddelovac()


def generovani_cisla() -> str:
    list_cislic_int = [0]
    while list_cislic_int[0] == 0:
        list_cislic_int = random.sample(list(range(10)), 4)
    list_cislic_str = [str(i) for i in list_cislic_int]
    hadane_cislo = ''.join(list_cislic_str)
    return hadane_cislo


hadanka = generovani_cisla()

hlavicka()

pocitadlo = 0
while True:
    bull = 0
    cow = 0
    zadane_cislo = input()
    if not zadane_cislo.isdigit():
        print('V zadaném čísle nejsou jen číslice.')
    elif len(zadane_cislo) != 4:
        print('Nebylo zadáno čtyřmístné číslo.')
    elif zadane_cislo[0] == '0':
        print('Zadané číslo začíná nulou.')
    elif len(zadane_cislo) != len(set(zadane_cislo)):
        print('V zadaném čísle jsou duplicitní číslice.')
    else:
        pocitadlo += 1
        if zadane_cislo == hadanka:
            print(f'Správně, uhádl jsi číslo na {pocitadlo}. pokus.')
            oddelovac()
            break
        else:
            for index, cislice in enumerate(zadane_cislo):
                if cislice in hadanka:
                    if cislice == hadanka[index]:
                        bull += 1
                    else:
                        cow += 1
            if bull == 1 and cow == 1:
                print(f'{bull} bull, {cow} cow')
                oddelovac()
            elif bull == 1 and cow != 1:
                print(f'{bull} bull, {cow} cows')
                oddelovac()
            elif bull != 1 and cow == 1:
                print(f'{bull} bulls, {cow} cow')
                oddelovac()
            else:
                print(f'{bull} bulls, {cow} cows')
                oddelovac()
