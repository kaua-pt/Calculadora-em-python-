from tkinter import *
from tkinter import font
from typing import Sized

# relief="solid",   há outros tipos, como groove, flat, raised, sunken,ridge

stringtoda = ""  # string base para colocar o resultado


def mostrar_numeros(adicionar):  # funcao que recebe as strings e coloca-as no resultado

    global stringtoda  # importa a string global para dentro de si

    if(adicionar != "="):  # se for diferente de resultado
        stringtoda = stringtoda + adicionar
        # string label absorve a string toda para ser exibido na tela posteirormente
        stringlabel.set(stringtoda)
    else:
        realizarconta(stringtoda)  # calcula


def realizarconta(conta):
    try:
        resultado = eval(conta)  # metodo para realizar conta com string

    except ZeroDivisionError:  # se for uma divisao por 0
        resultado = "Erro: Não se divide por 0"

    with open("registros.txt", "a+") as registro:
        registro.write(conta + " = " + str(resultado) + '\n')

    stringlabel.set(resultado)  # joga o resultado na tela


def limpar():
    # importa novamente a string global para de fato reseta-la fora da f(x)
    global stringtoda
    stringtoda = ""  # default
    stringlabel.set(stringtoda)  # coloca na tela


inicio = Tk()                                   # estruturas básica
inicio.title("Calculadora")                     # colocar título
# se pode redimensionar a janela, pode-se colocar 0 e 1
inicio.resizable(TRUE, True)
# tamanho do quadrado, largura por altura em string, o + indica o local onde ela aparece inicialmente
inicio.geometry("314x470+900+50")
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

fundo = Label(inicio)
fundo.place(x=0, y=0, relheight=1, relwidth=1)

# colocar tabela dos resultados

resultado = Frame(inicio,
                  bg='#808080',
                  width=400,
                  height=90).grid(column=0, row=0)

tabela = Frame(inicio,
               bg='#333333',
               width=400,
               height=410).grid(column=0, row=1)

# colocar botões
botao1 = Button(tabela,
                text="Limpar tela",
                height=4,
                width=31,
                command=lambda: limpar()).place(x=6, y=95)
botao1 = Button(tabela,
                text="/",
                height=4,
                width=9,
                bg="#FF7F00",
                command=lambda: mostrar_numeros('/')).place(x=235, y=95)
botao1 = Button(tabela,
                text="*",
                height=4,
                width=9,
                bg="#FF7F00",
                command=lambda: mostrar_numeros("*")).place(x=235, y=170)
botao1 = Button(tabela,
                text="-",
                height=4,
                width=9,
                bg="#FF7F00",
                command=lambda: mostrar_numeros("-")).place(x=235, y=245)
botao1 = Button(tabela,
                text="+",
                height=4,
                width=9,
                bg="#FF7F00",
                command=lambda: mostrar_numeros("+")).place(x=235, y=320)
botao1 = Button(tabela,
                text="9",
                height=4,
                width=9,
                command=lambda: mostrar_numeros("9")).place(x=158, y=170)
botao1 = Button(tabela,
                text="8",
                height=4,
                width=9,
                command=lambda: mostrar_numeros("8")).place(x=82, y=170)
botao1 = Button(tabela,
                text="7",
                height=4,
                width=9,
                command=lambda: mostrar_numeros("7")).place(x=6, y=170)
botao1 = Button(tabela,
                text="6",
                height=4,
                width=9,
                command=lambda: mostrar_numeros("6")).place(x=158, y=245)
botao1 = Button(tabela,
                text="5",
                height=4,
                width=9,
                command=lambda: mostrar_numeros("5")).place(x=82, y=245)
botao1 = Button(tabela, text="4",
                height=4,
                width=9,
                command=lambda: mostrar_numeros("4")).place(x=6, y=245)
botao1 = Button(tabela,
                text="3",
                height=4,
                width=9,
                command=lambda: mostrar_numeros("3")).place(x=158, y=320)
botao1 = Button(tabela,
                text="2",
                height=4,
                width=9,
                command=lambda: mostrar_numeros("2")).place(x=82, y=320)
botao1 = Button(tabela,
                text="1",
                height=4,
                width=9,
                command=lambda: mostrar_numeros("1")).place(x=6, y=320)
botao1 = Button(tabela,
                text="0",
                height=4,
                width=20,
                command=lambda: mostrar_numeros("0")).place(x=6, y=395)
botao1 = Button(tabela,
                text=",",
                height=4,
                width=9,
                command=lambda: mostrar_numeros(",")).place(x=158, y=395)
botao1 = Button(tabela,
                text="=",
                height=4,
                width=9,
                bg="#FF7F00",
                command=lambda: mostrar_numeros("=")).place(x=235, y=395)

stringlabel = StringVar()  # para colocar a string na text variable e printar na tela

visor = Label(resultado,
              textvariable=stringlabel,  # imprime o resultado na tela
              height=4,
              width=34,
              anchor=E,
              font='18').place(x=2, y=10)

inicio.mainloop()
