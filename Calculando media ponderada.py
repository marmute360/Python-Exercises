print("------------------------------------------------------")
print("---           Calculando média ponderada           ---")
print("------------------------------------------------------")


CodAln = int(input("Informe o código do aluno...:"))
Nota1 = float(input("digite a maior e primeira nota...:"))
Nota2 = float(input("digite a segunda nota...:"))
Nota3 = float(input("digite a terceira nota...:"))
print("======================================================")
MediaPond = (Nota1 * 4 + Nota2 * 3 + Nota3 * 3)/ 4 + 3 +3

if(MediaPond >= 5):

   print("Sua média foi", MediaPond, "Parabéns, você foi aprovado!!")

else:

   print("Sua média foi", MediaPond, "Infelizmente, você foi reprovado")
