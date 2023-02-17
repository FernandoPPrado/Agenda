from tkinter import *
import sqlite3


class Funcs:
    def limpar_tela(self):
        self.caixa_codigo.delete(0, END)
        self.caixa_nome.delete(0, END)
        self.caixa_email.delete(0, END)
        self.caixa_telefone.delete(0, END)

    def dados_conectar(self):
        self.conectar = sqlite3.connect('Usuarios.bd')
        self.cursor = self.conectar.cursor()
        print('Conectando ao banco')

    def dados_desconectar(self):
        self.conectar.close()
        print('Desconectado')

    def montar_tabela(self):
        self.dados_conectar()

        # criar tabela pessoas
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos(
        cod INTEGER PRIMARY KEY,
        nome_usuario VARCHAR(40) NOT NULL,
        email VARCHAR(255),
        telefone VARCHAR(20));
        ''')
        self.conectar.commit()
        self.dados_desconectar()

    def variaveis(self):
        self.codigo = self.caixa_codigo.get()
        self.nome = self.caixa_nome.get()
        self.email = self.caixa_email.get()
        self.telefone = self.caixa_telefone.get()

    def buscar_usuarios(self):
        self.dados_conectar()
        self.lista_frame1.delete(*self.lista_frame1.get_children())
        self.caixa_nome.insert(END, '%')
        nome = self.caixa_nome.get()
        self.cursor.execute("""
            SELECT cod, nome_usuario, email, telefone FROM contatos
            WHERE nome_usuario LIKE '%s' ORDER BY nome_usuario ASC""" % nome)

        var_nomes = self.cursor.fetchall()

        for i in var_nomes:
            self.lista_frame1.insert('', END, values=i)

        self.limpar_tela()
        self.dados_desconectar()

    def add_usuario(self):
        self.variaveis()
        self.dados_conectar()
        self.cursor.execute("""
            INSERT INTO contatos (nome_usuario, email, telefone)
            VALUES(?,?,?)""", (self.nome, self.email, self.telefone))

        self.conectar.commit()
        self.dados_desconectar()
        self.busca()
        self.limpar_tela()

    def busca(self):
        self.lista_frame1.delete(*self.lista_frame1.get_children())
        self.dados_conectar()
        lista = self.cursor.execute(""" 
            SELECT cod, nome_usuario, telefone, email FROM contatos
            ORDER BY nome_usuario ASC
        """)

        for i in lista:
            self.lista_frame1.insert('', END, values=i)
        self.dados_desconectar()

    def duploclique(self, event):
        self.limpar_tela()
        self.lista_frame1.selection()

        for n in self.lista_frame1.selection():
            col1, col2, col3, col4 = self.lista_frame1.item(n, 'values')
            self.caixa_codigo.insert(END, col1)
            self.caixa_nome.insert(END, col2)
            self.caixa_email.insert(END, col4)
            self.caixa_telefone.insert(END, col3)

    def deletarcontato(self):
        self.variaveis()
        self.dados_conectar()

        self.cursor.execute(
            """ DELETE FROM contatos WHERE cod = ? """, (self.codigo, ))
        self.conectar.commit()

        self.dados_desconectar()
        self.limpar_tela()
        self.busca()
