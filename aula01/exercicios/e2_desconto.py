# Crie 2 variáveis:
#   - cliente_vip
#   - cupom_desconto
#
# Ao final, imprima se o cliente tem direito ao desconto.
# O cliente tem direito ao desconto se for cliente VIP, mas
# também pode ter se possuir um cupom de desconto.

cliente_vip = True
cupom_desconto = False

if cliente_vip == True or cupom_desconto == True:
    print('Tem desconto')
else:
    print('Não tem Desconto')