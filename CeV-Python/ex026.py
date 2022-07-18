#aparição de uma letra na frase
#quantas e onde essa letra apareceu primeiro e por último

frase = input("Diga uma frase: ").strip().lower()
print(f"a letra 'a' apareceu {frase.count('a')} vezes")
print(f"a primeira letra está na posição {frase.find('a')+1}")
print(f"e apareceu pela última na {frase.rfind('a')+1}")