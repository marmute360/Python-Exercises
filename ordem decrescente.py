#5. Que leia três números e mostre-os em ordem decrescente.

print("------------------------------------------------------------------")
print("---    Lendo três números e mostrando em ordem decrescente     ---")
print("------------------------------------------------------------------")

Nr1 = int(input("Informe o primeiro número...:"))
Nr2 = int(input("Informe o segundo número...:"))
Nr3 = int(input("Informe o terceiro número...:"))

numeros = [ '10', '20', '30']
numeros.sort(numeros, key=int, reversed=True)

print(numeros)
