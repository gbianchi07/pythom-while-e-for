n = int(input('informe a quantidade de numeros: '))

cont = 1
somapar= 0
somaimpar=0
contapar = 0
contaimpar = 0


while cont <= n:
    numero = int(input('numero: '))
    if numero % 2 == 0:
        somapar += numero                       #somatorio dos pares 
        contapar += 1                           #conta a quantidade de pares
    else:
        somaimpar += numero                    #somatorio dos impares
        contaimpar += 1                        #conta a quantidade de impares
    cont += 1

if contapar> 0:
    mediapar = somapar / contapar
    print(f'a media dos pares: {mediapar}')
else:
    print('nao ha numeros pares')
if contaimpar >0:
    mediaimpar = somaimpar / contaimpar
    print(f'a media dos impares: {mediaimpar}')
else:
    print('nao ha numeros impares')


mediapar = somapar / contapar
mediaimpar = somaimpar / contaimpar
print(f'a media dos pares: {mediapar}')
print(f'a media dos impares: {mediaimpar}')