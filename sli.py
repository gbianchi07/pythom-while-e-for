numero = int(input('informe um numero: '))

fatorial = 1                    #acumuladora
while numero >= 1:
    fatorial *= numero
    numero -= 1

print(f'fatorial: {fatorial}')