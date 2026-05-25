"""Se conecta ao banco loja.db;

Crie uma tabela produtos com os campos id, nome, preco;

Insira 3 produtos diferentes;

Liste todos os produtos cadastrados."""

import sqlite3
#CONECTAR AO BANCO
def conectar():
    conn = sqlite3.connect('loja.db')
    return conn

        # TABELAS de CREATE

def criar_tabela_produto():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

def criar_tabela_cliente():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS cliente(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT NOT NULL,
                idade INTEGER
            )
        """
    )
    conn.commit()
    conn.close()


            #FUNÇÕES de INSERT

def criar_cliente(nome, idade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            INSERT INTO cliente (nome, idade)
            VALUES (?, ?)
        """, (nome, idade)
    )
    conn.commit()
    conn.close()

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT * FROM cliente
        """
    )
    clientes = cursor.fetchall()

    for cliente in clientes:
        print(cliente)

    conn.commit()
    conn.close()

def criar_produtos(nome, preco):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO produtos (nome, preco)
        VALUES (?, ?)
        """,
        (nome, preco),
    )
    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT * FROM produtos
        """
    )
    produtos = cursor.fetchall()

    for produto in produtos:
        print(produto)

    conn.commit()
    conn.close()