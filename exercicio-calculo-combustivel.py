litros = int(input('Entre com o numero de litros de combustivel vendido: \n'))
tipo = input('Entre com o tipo de combustivel (codificado da seguinte forma: A-álcool, G-gasolina): \n')

if tipo == 'A':
    if litros <= 20:
        desconto = 0.03 * litros
        preco = (2.10 * litros) - desconto
        print("O preco final é igual a ", preco," reais")

    else:
        desconto = 0.05 * litros
        preco = (2.10 * litros) - desconto
        print("O preco final é igual a ", preco," reais")

elif tipo == 'G':
    if litros <= 20:
        desconto = 0.04 * litros
        preco = (3.30 * litros) - desconto
        print("O preco final é igual a ", preco," reais")

    else:
        desconto = 0.06 * litros
        preco = (3.30 * litros) - desconto
        print("O preco final é igual a ", preco," reais")
