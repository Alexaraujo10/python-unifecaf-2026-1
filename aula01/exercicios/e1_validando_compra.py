# Crie 2 variáveis: 
#   -  compra_paga
#   -  produto_em_estoque
#
# Ao final imprima se o produto pode ou não ser vendido. 
# O produto apenas pode ser vendido se a compra já foi paga 
# e se houver produto no estoque

compra_paga = True
produdto_em_estoque = False

if compra_paga == True and produdto_em_estoque == True:
    print('Pode Vender')
else:
    print('nao pode vender')