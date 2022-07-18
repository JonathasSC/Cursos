frase = input("Digite uma frase: ").upper().strip()
frases = frase.split()
invertida = ' '.join(frases) 
invertida = invertida [::-1]
if invertida == frase :
    print("Essa frase é um palindromo")
else: 
    print ("Essa frase NÃO é um palindromo")