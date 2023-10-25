vet = []
soma = 0
N = int(input('Entre com uma quantidade: '))

for i in range(N):
    vet.append(int(input("Entre com um numero: ")))
    soma += vet[i]

print("A soma dos elementos é igual a: ", soma)