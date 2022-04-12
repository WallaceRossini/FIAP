minutos = int(input("INFORME OS MINUTOS ATUAIS:"))
fatorial = 1
x = 2

while x <= minutos:
  fatorial = fatorial*x
  x = x + 1

print("LIBERDADA" + str(fatorial))