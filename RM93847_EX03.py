selecao = 0
media = 0
backup_media = 0
total = 0
turma = ''
continua = 0

resposta = int(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES ?\n1 - SIM \n2 - NÃO\n"))
print("---------------------------------------")
while continua <= 1: 
  media = 0
  total = 0 
  if (resposta) == 1 : 
    selecao = 0
    turma = 'PAR'
  else:
    selecao = 1
    turma = 'ÍMPAR'

  for x in range(1,51):

    if(x%2) == selecao:

      nota = int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO " + str(x) + ": \n")) 
      total += nota
  media = total / 5
  backup_media = media
  print('MÉDIA DA TURMA ' + turma + ' ' + str(media))
  if resposta == 1 : 
    resposta = 0
  else:
    resposta = 1
  continua+=1

if resposta == 1 : 
  turma = 'PAR'
else:
  turma = 'ÍMPAR'
print("---------------------------------------")
if backup_media > media :
  print("MÉDIA MAIOR DA TURMA: " + turma)
else:
  print("MÉDIA MAIOR DA TURMA: " + turma)