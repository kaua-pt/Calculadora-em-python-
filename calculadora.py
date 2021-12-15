from tkinter import *
from funcoes import *
from PIL import ImageTk, Image

inicio = Tk()                                   # estruturas básica
inicio.title("Calculadora")                     # colocar título
# se pode redimensionar a janela, pode-se colocar 0 e 1
inicio.resizable(False, False)
# tamanho do quadrado, largura por altura em string, o + indica o local onde ela aparece inicialmente
inicio.geometry("350x600+900+50")
# inicio['bg'] = "Black" Coloca-se dessa forma para mudar a cor que deve ser em inglês
inicio.iconbitmap("images/calculadora.ico")     # colocar ícone
# Inicio.minsize("ZZZxZZZ") ou .maxsize("ZZZxZZZ") se o resizable for true, ele indica até
# O maximo de largura que você pode estender a tela
# .state("zoomed") abre o app em seu maxsize,("iconic") abre no minsize
# A função .winfo_screen...() ele te permite que você obtenha uma largura x comprimento padrão do windows
# se dividi-la por 2, temos o centro

# iniciofundo = ImageTk.PhotoImage(Image.open(
#   "images/fundo.jpg").resize((350, 600), Image.ANTIALIAS))  # colocar fundo, você abre a imagem, redimensiona a mesma
# colocar imagem
fundo = Label(inicio, bg='#494C4E')
fundo.place(x=0, y=0, relheight=1, relwidth=1)

bemvindo = Label(inicio,
                 text=("Bem vindo a calculadora"),  # printar imagem
                 font=("Arial"),
                 fg="Black",
                 bg="white",
                 bd=2,
                 relief="solid",  # há outros tipos, como groove, flat, raised, sunken,ridge
                 height=2,
                 width=25).pack(pady=50)

num1 = StringVar()
num2 = StringVar()

textonum1 = Label(inicio,
                  text=("1° Número:"),
                  bd=2,
                  relief="solid").place(x=48, y=120)

textonum2 = Label(inicio,
                  text=("2° Número:"),
                  bd=2,
                  relief="solid").place(x=228, y=120)

caixanum1 = Entry(inicio,
                  width=20,
                  textvariable=num1).place(x=20, y=150)

caixanum2 = Entry(inicio,
                  width=20,
                  textvariable=num2).place(x=200, y=150)

espaco = Frame(inicio,
               height=80,
               bd=2,
               relief="solid")
espaco.pack(pady=40, fill=X)  # fill serve para preencher todo

botaoadd = Button(espaco,
                  text="Soma",
                  command=lambda: add(num1.get(), num2.get())).place(x=38, y=5)
botaosub = Button(espaco,
                  text="Subtração",
                  command=lambda: sub(num1.get(), num2.get())).place(x=150, y=20)
botaomult = Button(espaco,
                   text="Multiplicação",
                   command=lambda: mult(num1.get(), num2.get())).place(x=38, y=40)
botaodiv = Button(espaco,
                  text="Divisão",
                  command=lambda: div(num1.get(), num2.get())).place(x=260, y=5)
botaopot = Button(espaco,
                  text="Potenciação",
                  command=lambda: pot(num1.get(), num2.get())).place(x=260, y=40)

textoresultado = Label(inicio,
                       text=("Resultado:"),
                       bd=2,
                       relief="solid").place(x=150, y=280)

resultado = Label(inicio).place(x=175, y=310)
# o place ou grid também atuam como pack()
inicio.mainloop()
