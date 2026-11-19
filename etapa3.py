# Programa de cálculo de desconto e forma de pagamento

valor_compra = float(input("\nDigite o valor total da compra: "))
forma_pagamento = input("Digite a forma de pagamento (dinheiro/pix/cartão): ").lower()

if valor_compra <= 50:
    print(f"Total da compra: R$ {valor_compra:.2f}")
elif valor_compra > 50 and valor_compra <= 100:
    desconto = valor_compra * 0.05
    total_com_desconto = valor_compra - desconto
    print(f"\nTotal da compra: R$ {valor_compra:.2f}")
    print(f"Desconto de 5% aplicado: R$ {desconto:.2f}")
    print(f"Total com desconto: R$ {total_com_desconto:.2f}")
else:
    desconto = valor_compra * 0.10
    total_com_desconto = valor_compra - desconto
    print(f"Total da compra: R$ {valor_compra:.2f}")
    print(f"Desconto de 10% aplicado: R$ {desconto:.2f}")
    print(f"Total com desconto: R$ {total_com_desconto:.2f}")
   

if forma_pagamento == "dinheiro":
    print(f"Forma de pagamento: {forma_pagamento}")
    print("Ganhou um picolé de brinde!")
elif forma_pagamento != "dinheiro" and forma_pagamento != "pix" and forma_pagamento != "cartão":
    print("Forma de pagamento inválida. Por favor, escolha entre dinheiro, pix ou cartão.")
else:
    print(f"Forma de pagamento: {forma_pagamento}")