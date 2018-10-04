obrazec = input('Počítám čtverec nebo kruh? ')
square = obrazec == 'čtverec'
circle = obrazec == 'kruh'
if square == True:  # komentář
    strana = float(input('Zadej stranu čtverce: '))
    print()
    print("Obvod čtverce se stranou", strana, "cm je", 4 * strana, "cm.")
    print("Obsah čtverce se stranou", strana, "cm je", strana ** 2, "cm2.")
elif circle == True:
    polomer = float(input('Zadej poloměr kruhu: '))
    from math import pi
    print()
    print("Obvod kruhu s poloměrem", polomer, "cm je", 2 * pi * polomer, "cm.")
    print("Obsah kruhu s poloměrem", polomer, "cm je", pi * polomer ** 2, "cm2.")
else:
    print('Špatná volba')
print()
print()
print('Nashledanou...')
