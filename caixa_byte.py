produtos = ["Hambúrguer", "X-Bacon", "Refrigerante", "Suco de caju"]
precos = [18.50, 24.00, 6.00, 8.00]

lanchonete = "Lanchonete Byte"
atendente = input("Digite o nome do atendente: ")
cliente = input("Digite o nome do cliente: ")

print(f"\nBem-vindo à {lanchonete}!")
print(f"Atendente: {atendente}")
print(f"Cliente: {cliente}")

print("\n--- Cardápio ---")
for i in range(len(produtos)):
    print(f"{i + 1}. {produtos[i]} - R$ {precos[i]:.2f}")

pedido = []
itens_pedido = []
qut_itens = int(input("\nQuantos itens diferentes deseja pedir? "))

for i in range(qut_itens):
    numero_produto = int(input("Digite o número do produto: "))
    quantidade = int(input("Digite a quantidade: "))

    if numero_produto < 1 or numero_produto > len(produtos):
        print("Produto inválido")
    else:
        nome_produto = produtos[numero_produto - 1]
        preco_produto = precos[numero_produto - 1]
        valor_item = preco_produto * quantidade
        pedido.append(valor_item)
        itens_pedido.append(
            f"{nome_produto} x {quantidade} - R$ {valor_item:.2f}"
        )

subtotal = sum(pedido)
taxa_servico = subtotal * 0.10
valor_com_taxa = subtotal + taxa_servico

if valor_com_taxa > 100:
    desconto = valor_com_taxa * 0.10
elif valor_com_taxa > 50:
    desconto = valor_com_taxa * 0.05
else:
    desconto = 0

total = valor_com_taxa - desconto

forma_pagamento = input(
    "\nDigite a forma de pagamento (dinheiro/pix/cartão): "
).lower()

valor_pago = 0
troco = 0
if forma_pagamento not in ("dinheiro", "pix", "cartão"):
    print("Forma de pagamento inválida. Escolha dinheiro, pix ou cartão.")
elif forma_pagamento == "dinheiro":
    valor_pago = float(input("Digite o valor pago: R$ "))
    troco = valor_pago - total

print("\n" + "=" * 30)
print("       Cupom fiscal")
print("=" * 30)
print(f"Lanchonete: {lanchonete}")
print(f"Atendente: {atendente}")
print(f"Cliente: {cliente}")
print("-" * 30)

for item in itens_pedido:
    print(item)

print("-" * 30)
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Taxa de serviço (10%): R$ {taxa_servico:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total: R$ {total:.2f}")
print(f"Forma de pagamento: {forma_pagamento}")

if forma_pagamento == "dinheiro":
    print(f"Valor pago: R$ {valor_pago:.2f}")
    print(f"Troco: R$ {troco:.2f}")
    print("Ganhou um picolé de brinde!")
