# qualquer coisa

nume1= int(input("digite numero    "))
nume2= int(input("agora outro numero   "))
                 
operacao = int(input("Digite uma opção (1 para soma, 2 para subtração):   "))

if operacao == 1:
 resultado= nume1 + nume2
 print(resultado)

elif operacao == 2:
   resultado = nume1 - nume2
   print(resultado)
 
else:
  print("operação não executada")
