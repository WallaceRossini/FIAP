semana = ["SEGUNDA","TERÇA","QUARTA","QUINTA","SEXTA"]
votos = [0,0,0,0,0]

for x in range(5):
  votos[x] = int(input("QUANTIDADE DE VOTOS NA " + semana[x] +": "))

max_votos = max(votos)
dia = semana[votos.index(max_votos)]


print("DIA MAIS VOTADO: " + dia + " - " + str(max_votos) +" VOTOS")