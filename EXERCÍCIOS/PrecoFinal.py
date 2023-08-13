valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

total_hamburgueres = valorHamburguer * quantidadeHamburguer
total_bebidas = valorBebida * quantidadeBebida

preco_final = total_hamburgueres + total_bebidas

troco = valorPago - preco_final

print(f'O preço final do pedido é R$ {preco_final:.2f}. Seu troco é R$ {troco:.2f}')