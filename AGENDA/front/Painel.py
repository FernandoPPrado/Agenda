
from tkinter import *
from tkinter import ttk
from BACK.Funções import Funcs


janela = Tk()


class PAINEL(Funcs):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frame()
        self.labs()
        self.botoes()
        self.caixas_dados()
        self.lista_f1()
        self.montar_tabela()
        self.busca()
        janela.mainloop()

    def tela(self):
        self.janela.geometry('800x600+100+100')
        self.janela.title('AGENDA')
        self.janela['bg'] = '#304D63'
        self.janela.resizable(False, False)

    def frame(self):
        # Frame 1 (maior a esquerda) e suas proprieadades
        self.frame1 = Frame(
            self.janela, highlightbackground='#8db2b3', highlightthickness=3)
        self.frame1.place(x=10, y=10, width=385, height=580)
        self.frame1['bg'] = '#B2E7E8'

        # Frame 2 (menor superior) e suas proprieadades
        self.frame2 = Frame(
            self.janela, highlightbackground='#8db2b3', highlightthickness=3)
        self.frame2.place(x=405, y=10, width=385, height=285)
        self.frame2['bg'] = '#B2E7E8'

        # Frame 3 (menor inferior) e suas proprieadades
        self.frame3 = Frame(
            self.janela, highlightbackground='#8db2b3', highlightthickness=3)
        self.frame3.place(x=405, y=305, width=385, height=285)
        self.frame3['bg'] = '#B2E7E8'

    def botoes(self):
        # Criação do botão Salvar
        self.botao_salvar = Button(
            self.frame3, text='Salvar', command=self.add_usuario)
        # Estilo do botão
        self.botao_salvar.configure(
            bg='#304D63', fg='white', font=('TimesNewRoman', 10, 'bold'))
        self.botao_salvar.place(
            relx=0.76, rely=0.06, relheight=0.1, relwidth=0.2)

        # Criação do botão Apagar
        self.botao_apagar = Button(
            self.frame3, text='Apagar', command=self.deletarcontato)
        # Estilo do botão
        self.botao_apagar.configure(
            bg='#304D63', fg='white', font=('TimesNewRoman', 10, 'bold'))
        self.botao_apagar.place(
            relx=0.55, rely=0.06, relheight=0.1, relwidth=0.2)

        # Criação do botão Buscar
        self.botao_buscar = Button(
            self.frame3, text='Buscar', command=self.buscar_usuarios)
        # Estilo do botão
        self.botao_buscar.configure(
            bg='#304D63', fg='white', font=('TimesNewRoman', 10, 'bold'))
        self.botao_buscar.place(
            relx=0.25, rely=0.06, relheight=0.1, relwidth=0.2)

        # Criação do botão Limpar
        self.botao_limpar = Button(
            self.frame3, text='Limpar', command=self.limpar_tela)
        # Estilo do botão
        self.botao_limpar.configure(
            bg='#304D63', fg='white', font=('TimesNewRoman', 10, 'bold'))
        self.botao_limpar.place(
            relx=0.04, rely=0.06, relheight=0.1, relwidth=0.2)

    def labs(self):
        # Criação da legenda código
        self.lb_codigo = Label(self.frame2, text='Código')
        self.lb_codigo.configure(
            bg='#99c6c7', fg='black', font=('TimesNewRoman', 10,))
        self.lb_codigo.place(relx=0.02, rely=0.02,
                             relwidth=0.15, relheight=0.1)

        # Criação da legenda Nome
        self.lb_nome = Label(self.frame2, text='Nome')
        self.lb_nome.configure(
            bg='#99c6c7', fg='black', font=('TimesNewRoman', 10,))
        self.lb_nome.place(relx=0.19, rely=0.02,
                           relwidth=0.790, relheight=0.1)

        # Criação da legenda e-mail
        self.lb_email = Label(self.frame2, text='E-mail')
        self.lb_email.configure(
            bg='#99c6c7', fg='black', font=('TimesNewRoman', 10,))
        self.lb_email.place(relx=0.02, rely=0.32,
                            relwidth=0.955, relheight=0.1)

        # Criação da legenda telefone
        self.lb_telefone = Label(self.frame2, text='Telefone')
        self.lb_telefone.configure(
            bg='#99c6c7', fg='black', font=('TimesNewRoman', 10,))
        self.lb_telefone.place(relx=0.02, rely=0.62,
                               relwidth=0.955, relheight=0.1)

    def caixas_dados(self):
        # Criação das caixa código para entrada de dados
        self.caixa_codigo = Entry(self.frame2)
        self.caixa_codigo.configure(
            bg='#abddde', font=('TimesNewRoman', 10, 'bold'))
        self.caixa_codigo.place(relx=0.02, rely=0.16,
                                relwidth=0.15, relheight=0.1)

        # Criação das caixa nome para entrada de dados
        self.caixa_nome = Entry(self.frame2)
        self.caixa_nome.configure(
            bg='#abddde', font=('TimesNewRoman', 10, 'bold'))
        self.caixa_nome.place(relx=0.19, rely=0.16,
                              relwidth=0.790, relheight=0.1)

        # Criação das caixa e-mail para entrada de dados
        self.caixa_email = Entry(self.frame2)
        self.caixa_email.configure(
            bg='#abddde', font=('TimesNewRoman', 10, 'bold'))
        self.caixa_email.place(relx=0.02, rely=0.465,
                               relwidth=0.955, relheight=0.1)

        # Criação das caixa cidade para entrada de dados
        self.caixa_telefone = Entry(self.frame2)
        self.caixa_telefone.configure(
            bg='#abddde', font=('TimesNewRoman', 10, 'bold'))
        self.caixa_telefone.place(relx=0.02, rely=0.770,
                                  relwidth=0.955, relheight=0.1)

    def lista_f1(self):
        self.lista_frame1 = ttk.Treeview(
            self.frame1, height=3, columns=('coll1', 'coll2', 'coll3', 'coll4'))

        self.lista_frame1.heading('#0', text='')
        self.lista_frame1.heading('#1', text='CD')
        self.lista_frame1.heading('#2', text='Nome')
        self.lista_frame1.heading('#3', text='Telefone')
        self.lista_frame1.heading('#4', text='E-Mail')

        self.lista_frame1.column('#0', width=1)
        self.lista_frame1.column('#1', width=25)
        self.lista_frame1.column('#2', width=120)
        self.lista_frame1.column('#3', width=70)
        self.lista_frame1.column('#4', width=140)

        self.lista_frame1.place(x=0.2, y=0.1, relheight=1, relwidth=0.95)

        # Definindo o Scroll

        self.scrol = Scrollbar(self.frame1, orient='vertical')
        self.lista_frame1.configure(yscroll=self.scrol.set)
        self.scrol.place(relx=0.95, y=0.1, relheight=1, relwidth=0.05)

        self.lista_frame1.bind("<Double-1>", self.duploclique)


PAINEL()
