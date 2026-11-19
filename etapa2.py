# Resume de pedido, pergunta a quantidade de cada produto, calcula o subtotal, 
# taxa de serviço, total, valor pago, troco, quantidade de sacolas cheias e itens soltos. 

qut_hamburguer = int(input("\nDigite a quantidade de hambúrgueres: "))
qut_refri = int(input("Digite a quantidade de refrigerantes: "))

subtotal_hamburguer = qut_hamburguer * 18.50
subtotal_refri = qut_refri * 6.00
subtotal = subtotal_hamburguer + subtotal_refri
taxa_servico = subtotal * 0.10
total = subtotal + taxa_servico

valor_pago = float(input("\nValor pago: "))

troco = valor_pago - total

qut_itens = qut_hamburguer + qut_refri

sacolas_cheias = qut_itens // 3
itens_soltos = qut_itens % 3

print("\n"+"="*30)
print("      Resumo do pedido:")
print("="*30)
print(f"Quantidade de hambúrgueres: {qut_hamburguer}")
print(f"Quantidade de refrigerantes: {qut_refri}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Taxa de serviço (10%): R$ {taxa_servico:.2f}")
print(f"Total: R$ {total:.2f}")
print(f"Valor pago: R$ {valor_pago:.2f}")
print(f"Troco: R$ {troco:.2f}")
print(f"Sacolas cheias: {sacolas_cheias} | Itens soltos: {itens_soltos}")