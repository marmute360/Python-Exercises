print("------------------------------------------------------------")
print("---  CALCULANDO GASTOS DE COMBUSTIVEL EM UMA VIAGEM       --")
print("------------------------------------------------------------")

ValorGas=float(input("Preço do Litro da Gasolina ============>"));
Dist=float(input("Distancia percorrida da Viagem em KM ====>"));

gasto= (Dist/15) * ValorGas;

print('Gastou um total de R$ ', gasto);

print(" ");
exit();
