nivel = ["BASIC","SILVER","GOLD","PLATINUM"]
porcentagem = [0.3,0.2,0.1,0.05]

print("NÍVEIS:")
for x in range(4):
  print(str(x) + " - " +nivel[x])
selecao = int(input("INFORME SEU NÍVEL: "))
faturamento = float(input("INFORME SEU FATURAMENTO: "))

pagar = faturamento * porcentagem[selecao]


print("PLANO:" + nivel[selecao])
print("FATURAMENTO R$:" + str(faturamento))
print("DEVERÁ PAGAR R$:" + str(pagar))