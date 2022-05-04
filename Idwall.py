import datetime

def formatacao(site=None,senha=None,ajudaSenha=None,numeroTelefone=None,nome=None,email=None,dataVazamento=None):
  v = dict()
  v['site'] = site
  v['senha'] = senha
  v['nome'] = nome
  v['ajudaSenha'] = ajudaSenha
  v['numeroTelefone'] = numeroTelefone
  v['nome'] = nome 
  v['email'] = email
  v['dataVazamento'] = dataVazamento
  return v

canva = formatacao('Canva','12345',None,None,'João','joao@email.com',datetime.datetime(2019,5,1).strftime("%Y-%b"))
hurb = formatacao('Hurb','12345',None,'99999-9999','João','joao@email.com',datetime.datetime(2019,3,1).strftime("%Y-%b"))
adobe = formatacao('Adobe','12345','12eas',None,'João','joao@email.com',datetime.datetime(2013,10,1).strftime("%Y-%b"))
apollo = formatacao('Apollo',None,None,'99999-9999','João','joao@email.com',datetime.datetime(2018,7,1).strftime("%Y-%b"))
pdl = formatacao('PDL',None,None,'99999-9999','João','joao@email.com',datetime.datetime(2019,10,1).strftime("%Y-%b"))
 

rank = []
dados = [canva,hurb,adobe,apollo,pdl]

for i in range(0,5):
  n=0
  vazamento = []
  if(dados[i]['senha'] != None):
      n+= 1
      vazamento.append('senha')
  if(dados[i]['ajudaSenha'] != None):
      n+= 1
      vazamento.append('ajuda de senha')
  if(dados[i]['numeroTelefone'] != None):
      n+= 1
      vazamento.append('número de telefone')
  if(dados[i]['nome'] != None):
      n+= 1
      vazamento.append('nome')
  if(dados[i]['email'] != None):
      n+= 1
      vazamento.append('email')
  rank.append({'total':n,'empresa':dados[i]['site'],'dados':vazamento,'dataVazamento':dados[i]['dataVazamento']})
    
for j in range(0,5):
  print('Emprasa: {}\nNúmero de dados vazados: {}\nDados Vazados:{}\nData de Vazamento:{}\n------------------'.format(rank[j]['empresa'],rank[j]['total'],rank[j]['dados'],rank[j]['dataVazamento']))



## critérios
#1 - senha
#2 - ajuda da senha
#3 - numero de telefone
#4 - nomes 
#5 - email
#6 - data de vazamento 


