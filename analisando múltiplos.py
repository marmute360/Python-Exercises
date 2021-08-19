print("------------------------------------------------------------")
print("---     DESCOBRINDO SE DOIS NÚMEROS SÃO MULTIPLOS        ---")


n1 = float(input('Digite primeiro número: '))
n2 = float(input('Digite segundo número: '))

if (n1%n2 == 0) or (n2%n1 == 0):
    print('São múltiplos')
else:
    print('Não são múltiplos')
