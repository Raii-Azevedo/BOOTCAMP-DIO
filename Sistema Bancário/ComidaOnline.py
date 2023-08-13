n = int(input())

total = 0
pedidos = []
for _ in range(n):
    nome, valor = input().split()
    total += float(valor)
    pedidos.append((nome, float(valor)))

cupom = input()

if cupom == "10%":
    desconto = total * 0.10
elif cupom == "20%":
    desconto = total * 0.20
else:
    desconto = 0

valor_total_com_desconto = total - desconto

print(f"Valor total: {valor_total_com_desconto:.2f}")
