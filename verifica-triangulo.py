numero1 = int(input('Entre com o primeiro numero: \n'))
numero2 = int(input('Entre com o segundo numero: \n'))
numero3 = int(input('Entre com o terceiro numero: \n'))

if(numero1 > numero2 + numero3 or numero2 > numero1 + numero3 or numero3 > numero1+ numero2):
    print("Os valores inseridos não formam um triangulo")

elif(numero1 == numero2 and numero1 == numero3):
    print("Os valores formam um triangulo equilátero")

elif(numero1 == numero2 or numero2 == numero3 or numero3 == numero1):
    print("Os valores digitados formam um triangulo Isóceles")

elif(numero1 != numero2 and numero1 != numero3 and numero2 != numero3):
    print("Os valores digitados formam um triangulo escaleno")