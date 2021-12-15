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


bemvindo = Label(inicio, text=("Bem vindo a calculadora"),
                 font=("Arial"), fg="Black").pack(pady=60)
botaoadd = Button(inicio, text="Soma",
                  command=lambda: add(), Y=20, x=10).pack()
botaosub = Button(inicio, text="Subtração", command=lambda: sub()).pack()
botaomult = Button(inicio, text="Multiplicação", command=lambda: mult()).pack()
botaodiv = Button(inicio, text="Divisão", command=lambda: div()).pack()
botaopot = Button(inicio, text="Potenciação", command=lambda: pot()).pack()

inicio.mainloop()
