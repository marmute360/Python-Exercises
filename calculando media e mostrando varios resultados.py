#4. Calcule a média aritmética das 3 notas de um aluno e mostre, além do
#valor da média, uma mensagem de "Aprovado", caso a média seja
#igual ou superior a 7, a mensagem “em prova final” caso
#a média seja menor que 7 e maior ou igual a 4 e "reprovado", caso contrário.

print("------------------------------------------------------------------")
print("---      Calculando média e mostrando variados resultados      ---")
print("------------------------------------------------------------------")

Nota1 = float(input("Digite a primeira nota...: "))
Nota2 = float(input("Digite a segunda nota...: "))
Nota3 = float(input("Digite a terceira nota...: "))

Media = (Nota1 + Nota2 + Nota3)/3


if(Media >=7):
  print("Com a média igual a", Media, "você se encontra aprovado")

elif(Media>=4):
  print("Com a média igual a", Media, "você fará prova final")

else:
    print("Com a média igual a", Media, "você se encontra reprovado")

print(" ")
exit()

