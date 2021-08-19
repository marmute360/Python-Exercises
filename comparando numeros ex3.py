#3. Que leia dois números e indique se são iguais ou, se
#diferentes, mostre o maior e o menor (nesta sequência).

print("---------------------------------------------")
print("---        Comparando Números ex3         ---")
print("---------------------------------------------")

Nr1 = int(input("Informe o primeiro número...: "))
Nr2 = int(input("Informe o segundo número...: "))

if(Nr1 == Nr2):
    print("São iguais")

elif(Nr1 > Nr2):
    print(Nr1, "é maior e", Nr2, "é menor")

else:
    print(Nr2, "é maior e", Nr1, "é menor")
