km = float(input("Qual a distância da viagem? "))
if km > 200:
     preço = km * 0.50
     print (f"O preço da viagem deu R${preço}")
else:
   preço = km * 0.45
   print(f"O preço da viagem deu R${preço}")
