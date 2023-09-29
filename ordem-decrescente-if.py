numero1 = int(input('Entre com o primeiro numero: \n'))
numero2 = int(input('Entre com o segundo numero: \n'))
numero3 = int(input('Entre com o terceiro numero: \n'))


if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
    print('\nNumeros em ordem decrescente: \n')
    print("\n", numero1)
    print("\n", numero2)
    print("\n", numero3)

elif numero2 > numero1 and numero2 > numero3 and numero1 > numero3:
    print('\nNumeros em ordem decrescente:')
    print("\n", numero2)
    print("\n", numero1)
    print("\n", numero3)
    
elif numero3 > numero1 and numero3 > numero2 and numero2 > numero1: 
    print('\nNumeros em ordem decrescente:')
    print("\n", numero3)
    print("\n", numero2)
    print("\n", numero1)

elif numero1 > numero2 and numero2 < numero3 and numero1 > numero3:
    print('\nNumeros em ordem decrescente:')
    print("\n", numero1)
    print("\n", numero3)
    print("\n", numero2)

elif numero2 > numero1 and numero2> numero3 and numero3 > numero1:
    print('\nNumeros em ordem decrescente:')
    print("\n", numero2)
    print("\n", numero3)
    print("\n", numero1)

elif numero3 > numero2 and numero3 > numero1 and numero1 > numero2:
    print('\nNumeros em ordem decrescente:')
    print("\n", numero3)
    print("\n", numero1)
    print("\n", numero2)
