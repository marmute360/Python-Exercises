print("==============================================")
print("===      Calculando temperatura            ===")
print("==============================================")

x = 'S'
cont = 0
maior = 0
menor = 0

while x != 'N':
    z = int(input('Digite uma temperatura: '))
    cont += 1
    
    if cont == 1:
       maior = z
       menor = z
    else:
        if z > maior:
            maior = z
        if z < menor:
            menor = z

    x = str(input('Deseja continuar? S - Sim / N - Não  ')).upper()

print(f'A maior temperatura digitada foi {maior}.')
print(f'A menor temperatura digitada foi {menor}.')

