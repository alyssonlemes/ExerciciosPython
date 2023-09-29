numero1 = int(input('Entre com o primeiro numero: \n'))
numero2 = int(input('Entre com o segundo numero: \n'))

if numero1 > numero2:
    print('\nNumeros em ordem decrescente: \n')
    print("\n", numero1)
    print("\n", numero2)
elif numero2 > numero1:
    print('\nNumeros em ordem decrescente:')
    print("\n", numero2)
    print("\n", numero1)
else: 
    print('\nOs numeros digitados são iguais')