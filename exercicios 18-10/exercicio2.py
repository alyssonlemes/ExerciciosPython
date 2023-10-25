vet = []
cont = 0
somaPar = 0
N = int(input('Entre com uma quantidade: '))

for i in range(N):
    vet.append(int(input("Entre com um numero: ")))
    if vet[i] % 2 == 0:
        somaPar +=vet[i]
        cont += 1
  

print("A soma dos elementos é igual a: ", somaPar / cont)