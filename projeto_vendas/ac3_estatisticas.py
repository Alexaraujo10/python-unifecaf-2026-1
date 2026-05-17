# Avaliação Continuada 3 - 1 ponto
# PROJETO DE VENDAS - parte 1
# Exercicios de estatisticas de vendas.
# Entrega - dia 17/05/2026
from banco_de_dados.conexao import conectar, fechar_conexao
from datetime import datetime

def total_vendas_periodo():
    # Exercicio 1: calcular o valor total vendido em um periodo usando vendas.valor_final.
    conexao = conectar()

    cursor = conexao.cursor()

    query = """
    SELECT SUM(vendas.valor_final) AS total_vendas
    FROM vendas;
    """

    cursor.execute(query)

    resultado = cursor.fetchall()
    print('\n=== TOTAL DE VENDAS POR PERIODO ===')
    for vendas in resultado:
        print(f"Total: {vendas[0]}")


    fechar_conexao(conexao)

    return resultado
    


def qtd_vendas_por_vendedor():
    # Exercicio 2: contar quantas vendas cada vendedor realizou usando vendas.id_vendedor.
    conexao = conectar()

    cursor = conexao.cursor()

    query = """
    SELECT vendedores.nome,
    COUNT(*) AS qtde_vendas
    FROM vendas
    INNER JOIN vendedores
        ON vendas.id_vendedor = vendedores.id
    GROUP BY vendedores.nome;
    """

    cursor.execute(query)

    resultado = cursor.fetchall()

    print('\n=== TOTAL DE VENDAS POR VENDEDOR ===')
    for vendedor in resultado:
        print(f"Vendedor: {vendedor[0]} | qtde_vendas: {vendedor[1]}")

    fechar_conexao(conexao)

    return resultado


def ticket_medio_geral():

    conexao = conectar()

    cursor = conexao.cursor()

    query = """
    SELECT AVG(vendas.valor_final) AS ticket_medio
    FROM vendas;
    """

    cursor.execute(query)

    resultado = cursor.fetchall()
    print('\n=== TICKET MEDIO ===')
    for ticket in resultado:
        print(f"Ticket Medio: {ticket[0]}")


    fechar_conexao(conexao)

    return resultado

def ticket_medio_por_vendedor():
    conexao = conectar()

    cursor = conexao.cursor()

    query = """
    SELECT vendedores.nome,
    AVG(vendas.valor_final) AS ticket_medio
    FROM vendas
    INNER JOIN vendedores
        ON vendas.id_vendedor = vendedores.id
    GROUP BY vendedores.nome
    ORDER BY ticket_medio DESC;
    """

    cursor.execute(query)

    resultado = cursor.fetchall()
    print('\n=== TICKET MEDIO POR VENDEDOR ===')
    for ticketmedio in resultado:
        print(f"Ticket Medio Por Vendedor: {ticketmedio[0]}")


    fechar_conexao(conexao)

    return resultado


def produto_mais_vendido_qtd():
    conexao = conectar()

    cursor = conexao.cursor()

    query = """
    SELECT produtos.descricao,
    SUM(vendas_produtos.quantidade) AS total_vendido
    FROM vendas_produtos
    INNER JOIN produtos
        ON vendas_produtos.id_produto = produtos.id
    GROUP BY produtos.descricao
    ORDER BY total_vendido DESC
    LIMIT 1;
    """

    cursor.execute(query)

    resultado = cursor.fetchall()
    print('\n=== PRODUTO MAIS VENDIDO ===')
    for prodmaisvend in resultado:
        print(f"Produto Mais Vendido: {prodmaisvend[0]} ")


    fechar_conexao(conexao)

    return resultado


def produto_mais_rentavel_valor():
    conexao = conectar()

    cursor = conexao.cursor()

    query = """
    SELECT produtos.descricao,
    SUM(vendas_produtos.valor_total) AS faturamento_total
    FROM vendas_produtos
    INNER JOIN produtos
        ON vendas_produtos.id_produto = produtos.id
    GROUP BY produtos.descricao
    ORDER BY faturamento_total DESC
    LIMIT 1;
    """

    cursor.execute(query)

    resultado = cursor.fetchall()
    print('\n=== PRODUTO MAIS RENTAVEL ===')
    for prodrentavel in resultado:
        print(f"Vendedor: {prodrentavel[0]}")


    fechar_conexao(conexao)

    return resultado

def total_descontos_aplicados():
    conexao = conectar()

    cursor = conexao.cursor()

    query = """
    SELECT SUM(vendas.desconto) AS total_desconto
    FROM vendas;
    """

    cursor.execute(query)

    resultado = cursor.fetchall()
    print('\n=== TOTAL DE DESCONTOS APLICADOS ===')
    for descontoaplicado in resultado:
        print(f"Vendedor: {descontoaplicado[0]} ")


    fechar_conexao(conexao)

    return resultado


def percentual_desconto_medio():
    conexao = conectar()

    cursor = conexao.cursor()

    query = """
    SELECT AVG((vendas.desconto / vendas.valor_final) * 100)
    AS percentual_medio_desconto
    FROM vendas
    WHERE vendas.valor_final > 0;
    """

    cursor.execute(query)

    resultado = cursor.fetchall()
    print('\n=== PERCENTUAL DE DESCONTO MEDIO ===')
    for descontomedio in resultado:
        print(f"Vendedor: {descontomedio[0]}")


    fechar_conexao(conexao)

    return resultado

def faturamento_por_dia():
   
    conexao = conectar()

    cursor = conexao.cursor()

    query = """
    SELECT DATE(vendas.data_e_hora) AS dia,
    SUM(vendas.valor_final) AS faturamento_total
    FROM vendas
    GROUP BY DATE(vendas.data_e_hora)
    ORDER BY dia ASC;
    """

    cursor.execute(query)

    resultado = cursor.fetchall()
    print('\n=== FATURAMENTO POR DIA ===')
    for fatpordia in resultado:
        print(f"Vendedor: {fatpordia[0]} ")


    fechar_conexao(conexao)

    return resultado

def top_3_vendedores_faturamento():
    conexao = conectar()

    cursor = conexao.cursor()

    query = """
    SELECT vendedores.nome,
    SUM(vendas.valor_final) AS faturamento_total
    FROM vendas
    INNER JOIN vendedores
        ON vendas.id_vendedor = vendedores.id
    GROUP BY vendedores.nome
    ORDER BY faturamento_total DESC
    LIMIT 3;
    """

    cursor.execute(query)

    resultado = cursor.fetchall()
    print('\n=== TOP VENDAS DO MES ===')
    for topvendas in resultado:
        print(f"Vendedor: {topvendas[0]} ")
   

    fechar_conexao(conexao)

    return resultado
def menu_relatorios():
    opcoes = {
        "1": ("Total de vendas por periodo", total_vendas_periodo),
        "2": ("Quantidade de vendas por vendedor", qtd_vendas_por_vendedor),
        "3": ("Ticket medio geral", ticket_medio_geral),
        "4": ("Ticket medio por vendedor", ticket_medio_por_vendedor),
        "5": ("Produto mais vendido por quantidade", produto_mais_vendido_qtd),
        "6": ("Produto mais rentavel por faturamento", produto_mais_rentavel_valor),
        "7": ("Total de descontos aplicados", total_descontos_aplicados),
        "8": ("Percentual medio de desconto", percentual_desconto_medio),
        "9": ("Faturamento por dia", faturamento_por_dia),
        "10": ("Top 3 vendedores por faturamento", top_3_vendedores_faturamento),
    }

    while True:
        print("\n=== MENU AC3 - RELATORIOS ===")
        for codigo, (descricao, _) in opcoes.items():
            print(f"{codigo} - {descricao}")
        print("0 - Voltar")

        escolha = input("Escolha uma opcao: ").strip()

        if escolha == "0":
            print("Voltando ao menu principal.")
        elif escolha == "1":
            total_vendas_periodo()
        elif escolha == "2":
            qtd_vendas_por_vendedor()
        elif escolha == "3":
            ticket_medio_geral()
        elif escolha == "4":
            ticket_medio_por_vendedor()
        elif escolha == "5":
            produto_mais_vendido_qtd()
        elif escolha == "6":
             produto_mais_rentavel_valor()
        elif escolha == "7":
             total_descontos_aplicados()
        elif escolha == "8":
             percentual_desconto_medio()
        elif escolha == "9":
             faturamento_por_dia()
        elif escolha == "10":
             top_3_vendedores_faturamento()
             break

        if escolha in opcoes:
            descricao, funcao = opcoes[escolha]
            print(f"\nGerando relatorio: {descricao}")
            resultado = funcao()

            if resultado is None:
                print("Relatorio em estrutura base (return vazio).")
            else:
                print(resultado)
        else:
            print("Opcao invalida. Tente novamente.")
menu_relatorios()