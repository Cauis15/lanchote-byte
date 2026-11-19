# Programa de cardápio de produtos, utilizando listas.

produtos = ["Hambúrguer", "X-Bacon", "Batata frita", "Refrigerante"]
precos = [18.50, 24.00, 12.00, 6.00]

print(f"\nPrimeiro: {produtos[0]} | Último: {produtos[-1]}")
print(f"Total  de produtos: {len(produtos)}")

produtos.append("Suco de Caju")
precos.append(8.00)
produtos.remove("Batata frita")
precos.remove(12.00)

print("Cardápio de produtos atualizado: ", produtos)

escolha = int(input("\nDigite o número de um produto do cardápio: "))

print(f"\n{produtos[escolha-1]} custa R$ {precos[escolha-1]:.2f}")