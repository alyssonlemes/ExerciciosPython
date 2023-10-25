vet = []
cont = 0
cont2 = 0
soma = 0
media = 0
N = int(input('Entre com uma quantidade de alunos: '))

for i in range(N):
    vet.append(int(input('Entre com a nota do aluno: ')))
    cont += 1
    soma +=  vet[i]

media = soma / cont

for i in range(N):
    if(vet[i]> media):
        cont2 += 1


print('A media da turma é igual a: ', media)
print('A quantidade de notas acima da media é igual a:  ', cont2)
    
  

