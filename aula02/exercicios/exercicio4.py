# Reescreva o algoritmo abaixo usando apenas operadores lógicos (and, or, not)
# sem utilizar comparação direta (==)

acesso_premium = False
assinatura_ativa = True

#if acesso_premium == assinatura_ativa:
 #   print("Acesso correto")
#else:
 #   print("Inconsistência detectada")

# seu código aqui abaixo:

if not(not(acesso_premium or assinatura_ativa)):
    print("Acesso Permitido")
else:
    print("Acesso Negado")