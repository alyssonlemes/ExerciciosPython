numero1 = int(input('Entre com o sexo do participante (1- Homem ou 2- Mulher): \n'))


if numero1 == 1:
   altura = float(input('Entre com a altura do participante: \n'))
   peso =  (72.7 * altura) - 58
   print("O peso ideal do participante seria igual a: ", peso)

elif numero1 == 2:
   altura = float(input('Entre com a altura da participante: \n'))
   peso = (62.1 * altura) - 44.7
   print("O peso ideal da participante seria igual a: ", peso)
   
else: 
   print('\nInsira um numero válido')