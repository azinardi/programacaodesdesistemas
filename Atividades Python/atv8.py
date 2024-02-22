num1 = int(input("Digite a aŕea a ser pintada em metros quadrados:"))

coberturaporlitro = 3
litrosporlata = 18
precoporlata = 80.00

litrosnecessarios = (num1 / coberturaporlitro)
latasnecessarias = (litrosnecessarios / litrosporlata)
precototal = (latasnecessarias * precoporlata)

print("A quantidade de latas necessárias é:", latasnecessarias)
print("O preço total será:", precototal)
