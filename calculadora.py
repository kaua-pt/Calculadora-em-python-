from tkinter import *
from funcoes import *
from PIL import ImageTk, Image

inicio = Tk()                                   # estruturas básica
inicio.title("Calculadora")                     # colocar título
# se pode redimensionar a janela, pode-se colocar 0 e 1
inicio.resizable(True, True)
# tamanho do quadrado, largura por altura em string, o + indica o local onde ela aparece inicialmente
inicio.geometry("350x600+900+50")
# inicio['bg'] = "Black" Coloca-se dessa forma para mudar a cor que deve ser em inglês
inicio.iconbitmap("images/calculadora.ico")     # colocar ícone
# inicio.minsize("ZZZxZZZ") ou .maxsize("ZZZxZZZ") se o resizable for true, ele indica até
# o maximo de largura que você pode estender a tela
# .state("zoomed") abre o app em seu maxsize,("iconic") abre no minsize

iniciofundo = ImageTk.PhotoImage(Image.open(
    "images/fundo.jpg").resize((350, 600), Image.ANTIALIAS))  # colocar fundo, você abre a imagem, redimensiona a mesma
# colocar imagem
fundo = Label(inicio, image=iniciofundo)
fundo.place(x=0, y=0, relheight=1, relwidth=1)


bemvindo = Label(inicio, text=("Bem vindo a calculadora"),  # printar imagem
                 font=("Arial"), fg="Black").pack(pady=60)

espaco = Frame(inicio, bg='#DF7A50', height=60)
espaco.pack(pady=40, fill=X)  # fill serve para preencher todo

botaoadd = Button(espaco, text="Soma", command=lambda: add()).place(
    x=38)  # o place ou grid também atuam como pack()
botaosub = Button(espaco, text="Subtração",
                  command=lambda: sub()).place(x=150, y=15)
botaomult = Button(espaco, text="Multiplicação",
                   command=lambda: mult()).place(x=38, y=30)
botaodiv = Button(espaco, text="Divisão",
                  command=lambda: div()).place(x=260)
botaopot = Button(espaco, text="Potenciação",
                  command=lambda: pot()).place(x=260, y=30)

inicio.mainloop()
