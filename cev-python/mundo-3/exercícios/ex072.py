lista = ("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quize","dezesseis","dezessete","dezoito","dezenove","vinte")

tam = len(lista)

resp = int(input("Digite um numero de 0 á 20: "))



while True:
    try:
        if resp <= tam:
            print(f"voce digitou o numero {lista[resp]}")
            break
           
    except (IndexError):
        while resp > 20:
            resp = int(input("tente novamente um numero de 0 a 20: "))
            
    