#2. Calcule a média aritmética das 3 notas de um aluno e mostre, além do valor da média, uma mensagem
#de "Aprovado", caso a média seja igual ou superior a 7, caso contrário "reprovado".


print("---------------------------------------------")
print("---      CALCULANDO MÉDIA ARITMÉTICA      ---")
print("---------------------------------------------")

Nota1 = float(input("Informe a primeira nota...: "))
Nota2 = float(input("Informe a segunda nota...: "))
Nota3 = float(input("Informe a terceira nota...: "))

Media = (Nota1 + Nota2 + Nota3)/3

if (Media >= 7):
    print("Aprovado")
    
else:
    print("Reprovado")

