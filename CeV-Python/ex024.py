#você nasceu na cidade que começa com "Santo"?
cidade = input("Qual cidade você nasceu?: ").strip()
cidade = cidade.upper()
cidadediv = cidade.split()
print("SANTO" in cidadediv[0])