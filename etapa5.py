

produtos = ["Hambúrguer", "X-Bacon", "Refrigerante", "Suco de caju"]
precos = [18.50, 24.00, 6.00, 8.00]
vendas_do_dia = [37.00, 55.50, 12.00, 120.00, 8.00, 74.50]


print(("-"*3),"Cardápio",("-"*3))
for i in range(len(produtos)):
	print(f"{i + 1}. {produtos[i]} - R$ {precos[i]:.2f}")


print("\n"+("-"*3),"Fechamento",("-"*3))
total_vendas = 0

for venda in vendas_do_dia:
	total_vendas += venda

print(f"Total vendido: R$ {total_vendas:.2f}")

media_vendas = total_vendas / len(vendas_do_dia)
print(f"Média por venda: R$ {media_vendas:.2f}")

vendas_acima_de_50 = 0
for venda in vendas_do_dia:
	if venda > 50.00:
		vendas_acima_de_50 += 1

print(f"Vendas acima de R$ 50: {vendas_acima_de_50}")





