# Avaliação Continuada 4 - 1 ponto
# PROJETO DE VENDAS - parte 2
# Exercicios de CRUD completo (Produtos, Vendedores e Vendas)
# Entrega - dia 24/05/2026
from banco_de_dados.conexao import conectar, fechar_conexao
from datetime import datetime

# PRODUTOS

def criar_produto():
    # Exercicio 1: cadastrar um novo produto na tabela produtos (descricao, preco).
    print('=== Adicione um Produto ===')
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        produto = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: '))

        cursor.execute(
            "INSERT INTO produtos (descricao, preco) VALUES (%s, %s)", 
            (produto, preco)
        )
        conexao.commit() 
        print("Produto registrado!")
       

    
    finally:
        cursor.close()
        fechar_conexao(conexao)    
    
    return


def listar_produtos():
    # Exercicio 2: listar todos os produtos cadastrados com id, descricao e preco.
    print('=== Lista de Produtos  ===')
    
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "select * from produtos"
        )
        print('Lista de Produtos:  ')

        produtos =  cursor.fetchall()
        for p in produtos:
            descricao, preco = p[1], p[2]
            print(f"{p[0]} | {descricao} | R$ {preco:.2f}")

    finally:
        cursor.close()
        fechar_conexao(conexao)
    return 

    


def atualizar_produto():
    # Exercicio 3: atualizar descricao e/ou preco de um produto existente por id.
    print('=== Atualize um Produto ===')

    while True: 
        try: 
            attproduto = input('Digite o novo nome: ')
            idproduto = int(input('Digite o id do produto: '))
            attpreco = float(input('Digite o novo preço: '))
            break
        except:
            print("Dados Invalidos, Tente Novamente!!")

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("update produtos set descricao = %s where id=%s ;", (attproduto, idproduto,))
        cursor.execute("update produtos set preco = %s where id=%s ;", (attpreco, idproduto,))
        conexao.commit()
        print("Produto atualizado com sucesso")
    finally:
        cursor.close()
        fechar_conexao(conexao)

    return


def excluir_produto():
    # Exercicio 4: excluir um produto por id, tratando dependencias em vendas_produtos.

        
    conexao = conectar()
    cursor = conexao.cursor()
    
    while True:
        try:
            delproduto = int(input('Digite o id do produto: '))
            break
        except:
            print("Id invalido!!")
        
    cursor.execute("select * from vendas where id= %s", (delproduto,) )
    produtos = cursor.fetchone()
    if not produtos:
        cursor.execute("DELETE FROM produtos WHERE id = %s", (delproduto,))
        print("Produto deletado")
    else: 
        print("O Produto nao pode ser apagado")

    conexao.commit()
    cursor.close()
    fechar_conexao(conexao)
    return


# VENDEDORES

def criar_vendedor():
    # Exercicio 5: cadastrar um novo vendedor na tabela vendedores.
    print("=== Registre um Vendedor ===")
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        vendedor = input('Digite o nome do Vendedor: ')

        cursor.execute(
            "INSERT INTO vendedores (nome ) VALUES (%s)", 
            (vendedor,)
        )
        conexao.commit() 
        print( "Vendedor registrado!")
    
    finally:
        cursor.close()
        fechar_conexao(conexao)    
    return


def listar_vendedores():
    # Exercicio 6: listar todos os vendedores cadastrados.
    print('=== Lista de vendedores  ===')
    
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "select * from vendedores"
        )
        print('Lista de Vendedores:  ')

        vendedores =  cursor.fetchall()
        for p in vendedores:
            nome = p[1]
            print(f"{p[0]} | {nome} ")

    finally:
        cursor.close()
        fechar_conexao(conexao)
    return 
    


def atualizar_vendedor():
    # Exercicio 7: atualizar o nome de um vendedor existente por id.
    print('=== Atualize um Vendedor ===')

    while True: 
        try: 
            attvendedor = input('Digite o novo nome: ')
            idvendedor = int(input('Digite o id do vendedor: '))
            
            break
        except:
            print("Dados Invalidos, Tente Novamente!!")

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("update vendedores set nome = %s where id=%s ;", (attvendedor, idvendedor,))

        conexao.commit()
        print("Vendedor atualizado com sucesso")
    finally:
        cursor.close()
        fechar_conexao(conexao)

    return


def excluir_vendedor():
    # Exercicio 8: excluir vendedor por id, validando se possui vendas vinculadas.
    print("=== Exclua um Vendedor === ")
    conexao = conectar()
    cursor = conexao.cursor()
    
    while True:
        try:
            delvendedor = int(input('Digite o id do vendedor: '))
            break
        except:
            print("Id invalido!!")
        
    cursor.execute("select * from vendas where id= %s", (delvendedor,) )
    vendedor = cursor.fetchone()
    if not vendedor:
        cursor.execute("DELETE FROM vendedores WHERE id = %s", (delvendedor,))
        print("Vendedor deletado")
    else: 
        print("O Vendedor nao pode ser apagado")

    conexao.commit()
    cursor.close()
    fechar_conexao(conexao)
    return


# VENDAS

def criar_venda_com_itens():
    # Exercicio 9: criar uma venda e inserir itens na tabela vendas_produtos com quantidade e valores.

    print("=== Registre uma Venda ===")
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        nomevenda= input('Digite o id do Vendedor: ')
        datavenda = datetime(input("Digite a data e a hora da venda: "))
        desconto = int(input("Se houve desconto, digite o total de desconto: "))
        valorfinal = int(input("Digite o Valor final da venda: "))


        cursor.execute(
            "INSERT INTO vendas (id_vendedor, data_e_hora, desconto, valor_final) VALUES (%s, %s, %s, %s),"
            (nomevenda, datavenda, desconto, valorfinal,)
        )
        conexao.commit() 
        print( "Venda registrado!")
    
    finally:
        cursor.close()
        fechar_conexao(conexao)    
    return


def listar_vendas_completas():
    # Exercicio 10: listar vendas com vendedor e itens (produto, quantidade, valor_unitario, valor_total).
    print('=== Lista Todas as Vendas  ===')
    
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "select * from vendas"
        )
        print('Lista de Vendas:  ')

        vendas =  cursor.fetchall()
        
        for p in vendas:
            id_vendedor, data_hora,desconto, valor_final = p[1], p[2], p[3], p[4]
            print(f"{p[0]} | {id_vendedor} | {data_hora} | {desconto} | {valor_final} ")

    finally:
        cursor.close()
        fechar_conexao(conexao)
    return


def atualizar_venda_e_itens():
    # Exercicio 11: atualizar dados da venda (desconto/valor_final) e seus itens.
    print('=== Atualize uma venda ===')

    while True: 
        try: 
            idvenda = int(input('Digite o id da venda: '))
            idvendedor = int(input("Digite o id do vendedor"))
            dtahrvenda = int(input('Digite a data e a hora da venda : '))
            descvenda = int(input("Se houver desconto, digite o desconto da venda: "))
            valorfinalvenda = int(input("Digite o valor final da venda: "))
            
            break
        except:
            print("Dados Invalidos, Tente Novamente!!")

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("update vendas set id = %s where id=%s ;", (idvendedor, idvenda,))
        cursor.execute("update vendas set data_e_hora = %s where id=%s", (dtahrvenda, idvenda))
        cursor.execute("update vendas set desconto = %s where id=%s",(descvenda, idvenda))
        cursor.execute("update vendas set valor_final = %s where id=%s", (valorfinalvenda, idvenda))

        conexao.commit()
        print("Vendedor atualizado com sucesso")
    finally:
        cursor.close()
        fechar_conexao(conexao)
    return


def excluir_venda():
    # Exercicio 12: excluir uma venda por id removendo primeiro os itens de vendas_produtos.
    print("=== Exclua uma Venda === ")
    conexao = conectar()
    cursor = conexao.cursor()
    
    while True:
        try:
            delvenda = int(input('Digite o id da venda: '))
            break
        except:
            print("Id invalido!!")
        
    cursor.execute("select * from vendas_produtos where id= %s", (delvenda,) )
    vendas = cursor.fetchone()
    if not vendas:
        cursor.execute("DELETE FROM vendas WHERE id = %s", (delvenda,))
        print("Venda deletado")
    else: 
        print(" A venda nao pode ser apagada")

    conexao.commit()
    cursor.close()
    fechar_conexao(conexao)
    return


def menu():
    opcoes = {
        "1": ("Criar produto", criar_produto),
        "2": ("Listar produtos", listar_produtos),
        "3": ("Atualizar produto", atualizar_produto),
        "4": ("Excluir produto", excluir_produto),
        "5": ("Criar vendedor", criar_vendedor),
        "6": ("Listar vendedores", listar_vendedores),
        "7": ("Atualizar vendedor", atualizar_vendedor),
        "8": ("Excluir vendedor", excluir_vendedor),
        "9": ("Criar venda com itens", criar_venda_com_itens),
        "10": ("Listar vendas completas", listar_vendas_completas),
        "11": ("Atualizar venda e itens", atualizar_venda_e_itens),
        "12": ("Excluir venda", excluir_venda),
    }

    while True:
        print("\n=== MENU AC4 - CRUD COMPLETO ===")
        for codigo, (descricao, _) in opcoes.items():
            print(f"{codigo} - {descricao}")
        print("0 - Voltar")

        escolha = input("Escolha uma opcao: ").strip()

        if escolha == "0":
            print("Voltando ao menu principal.")
            break

        if escolha in opcoes:
            descricao, funcao = opcoes[escolha]
            print(f"\nSelecionado: {descricao}")
            funcao()
            print("Exercicio em estrutura base (return vazio).")
        else:
            print("Opcao invalida. Tente novamente.")
menu()

