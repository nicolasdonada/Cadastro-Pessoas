import mysql.connector
from tkinter import *

class Cadastro:
    def __init__(self):
        self.bancodedados = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="amlnra409",
            database="cadastro"
        )
        
        self.cont = 0

        self.janela = Tk()
        self.janela.title("Cadastramento")
        self.janela.geometry("500x450")
        self.janela.config(bg="#333333")
        self.janela.resizable(width=False, height=False)
        self.interface()


        self.janela.mainloop()


    def interface(self):
        self.label1 = Label(self.janela, width=5, height=2, text="Nome:", bg="#333333", fg="white", font="Arial 15")
        self.label1.place(x=7, y=10)

        self.label2 = Label(self.janela, width=8, height=2, text="Profissão:", bg="#333333", fg="white", font="Arial 15")
        self.label2.place(x=6, y=60)

        self.label3 = Label(self.janela, width=9, height=2, text="Nascimento:", bg="#333333", fg="white", font="Arial 15")
        self.label3.place(x=10, y=110)

        self.label4 = Label(self.janela, width=5, height=2, text="Sexo:", bg="#333333", fg="white", font="Arial 15")
        self.label4.place(x=5, y=160)

        self.label5 = Label(self.janela, width=5, height=2, text="Peso:", bg="#333333", fg="white", font="Arial 15")
        self.label5.place(x=4, y=210)

        self.label6 = Label(self.janela, width=5, height=2, text="Altura:", bg="#333333", fg="white", font="Arial 15")
        self.label6.place(x=10, y=260)

        self.label7 = Label(self.janela, width=11, height=2, text="Nacionalidade:", bg="#333333", fg="white", font="Arial 15")
        self.label7.place(x=10, y=310)
        #------------------------------------------------------------------------

        labelnasci = Label(self.janela, width=12, height=2, text="Ex: 2000-01-01", bg="#333333", fg="white", font="Arial 12")
        labelnasci.place(x=235,y=116)

        labelsex = Label(self.janela, width=5, height=2, text="Ex: M/F", bg="#333333", fg="white", font="Arial 12")
        labelsex.place(x=173, y=167)

        labelpeso = Label(self.janela, width=7, height=2, text="Ex: 70.5", bg="#333333", fg="white", font="Arial 12")
        labelpeso.place(x=170, y=216)

        labelaltura = Label(self.janela, width=7, height=2, text="Ex: 1.70", bg="#333333", fg="white", font="Arial 12")
        labelaltura.place(x=180, y=267)
        #-------------------------------------------------------------------------

        self.entry1 = Entry(self.janela, width=15)
        self.entry1.place(x=80, y=28)
        

        self.entry2 = Entry(self.janela, width=15)
        self.entry2.place(x=110, y=78)
        

        self.entry3 = Entry(self.janela, width=15)
        self.entry3.place(x=130, y=128)
        

        self.entry4 = Entry(self.janela, width=15)
        self.entry4.place(x=70, y=178)
        

        self.entry5 = Entry(self.janela, width=15)
        self.entry5.place(x=70, y=228)
        

        self.entry6 = Entry(self.janela, width=15)
        self.entry6.place(x=80, y=278)
        

        self.entry7 = Entry(self.janela, width=15)
        self.entry7.place(x=150, y=328)
        
        
        #-------------------------------------------------------------------------

        botao = Button(self.janela, width=10, height=1, text="Cadastrar", fg="white", bg="gray", relief="flat", overrelief="sunken", font="Arial 10", command=lambda: self.cadastrar())
        botao.place(x=130, y=380)

        botao = Button(self.janela, width=10, height=1, text="Limpar", fg="white", bg="gray", relief="flat", overrelief="sunken", font="Arial 10", command=lambda: self.reset())
        botao.place(x=240, y=380)


    def reset(self):
        self.labelinfo.destroy()

        for entry_widget in [self.entry1, self.entry2, self.entry3, self.entry4, self.entry5, self.entry6, self.entry7]:
            entry_widget.delete(0, "end")

    def cadastrar(self):

        self.labelinfo = Label(self.janela, width=30, height=2, text="Cadastro feito com sucesso!!", bg="#333333", fg="green", font="Arial 15")
        self.labelinfo.place(x=180, y=20)

        self.cont += 1

        mycursor = self.bancodedados.cursor()

        self.nome = self.entry1.get()
        self.profissao = self.entry2.get()
        self.nascimento = str(self.entry3.get())
        self.sexo = str(self.entry4.get())
        self.peso = self.entry5.get().replace(",", ".")
        self.altura = self.entry6.get().replace(",", ".")
        self.nacionalidade = str(self.entry7.get())

        sql = "INSERT INTO gafanhotos (id, nome, profissao, nascimento, sexo, peso, altura, nacionalidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (self.cont, self.nome, self.profissao, self.nascimento, self.sexo, float(self.peso), float(self.altura), self.nacionalidade)


        mycursor.execute(sql, valores)
    
        self.bancodedados.commit()
  

cad = Cadastro()