numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    vegano = input() == "s"
    
    if vegano:
        tipoVegano = "Vegano"
    else:
        tipoVegano = "Não-vegano"

    print(f"Pedido {i}: {prato} ({tipoVegano}) - {calorias} calorias")
