from tkinter import *

# relief="solid",   há outros tipos, como groove, flat, raised, sunken,ridge


def mostrar_numeros():
    pass


inicio = Tk()                                   # estruturas básica
inicio.title("Calculadora")                     # colocar título
# se pode redimensionar a janela, pode-se colocar 0 e 1
inicio.resizable(True, True)
# tamanho do quadrado, largura por altura em string, o + indica o local onde ela aparece inicialmente
inicio.geometry("290x500+900+50")
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
botao1 = Button(tabela, text="Limpar tela",
                height=4, width=27).place(x=8, y=95)
botao1 = Button(tabela, text="/",
                height=4, width=9).place(x=210, y=95)
botao1 = Button(tabela, text="*",
                height=4, width=9).place(x=210, y=170)
botao1 = Button(tabela, text="-",
                height=4, width=9).place(x=210, y=245)
botao1 = Button(tabela, text="+",
                height=4, width=9).place(x=210, y=320)
botao1 = Button(tabela, text="Limpar tela",
                height=4, width=9).place(x=8, y=95)
botao1 = Button(tabela, text="Limpar tela",
                height=4, width=9).place(x=8, y=95)
botao1 = Button(tabela, text="Limpar tela",
                height=4, width=9).place(x=8, y=95)
botao1 = Button(tabela, text="Limpar tela",
                height=4, width=9).place(x=8, y=95)
botao1 = Button(tabela, text="Limpar tela",
                height=4, width=9).place(x=8, y=95)
botao1 = Button(tabela, text="Limpar tela",
                height=4, width=9).place(x=8, y=95)
botao1 = Button(tabela, text="Limpar tela",
                height=4, width=9).place(x=8, y=95)
botao1 = Button(tabela, text="Limpar tela",
                height=4, width=9).place(x=8, y=95)
botao1 = Button(tabela, text="Limpar tela",
                height=4, width=9).place(x=8, y=95)
botao1 = Button(tabela, text="Limpar tela",
                height=4, width=9).place(x=8, y=95)
botao1 = Button(tabela, text="Limpar tela",
                height=4, width=9).place(x=8, y=95)
botao1 = Button(tabela, text="=",
                height=4, width=9).place(x=210, y=395)


inicio.mainloop()
