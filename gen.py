from random import randrange

kdo = input('Celý tým, vývoj nebo produkt? ')
devs = kdo == 'vývoj'
disco = kdo == 'produkt'
team = kdo == 'tým'

if devs == True:
    cislo = randrange(1, 5) # Vybírá čísla 1-4
    if cislo == 1:
        print('Jirka')
    elif cislo == 2:
        print('Honza')
    elif cislo == 3:
        print('Markéta')
    elif cislo == 4:
        print('Dejv')
elif disco == True:
    cislo = randrange(5, 7) # Vybírá čísla 5-6
    if cislo == 5:
        print('Kačka')
    elif cislo == 6:
        print('Tomáš')
elif team == True:
    cislo = randrange(1, 8) # Vybírá čísla 1-7
    if cislo == 1:
        print('Jirka')
    elif cislo == 2:
        print('Honza')
    elif cislo == 3:
        print('Markéta')
    elif cislo == 4:
        print('Dejv')
    elif cislo == 5:
        print('Kačka')
    elif cislo == 6:
        print('Tomáš')
    elif cislo == 7:
        print('Michal')
