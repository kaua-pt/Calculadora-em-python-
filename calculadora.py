from tkinter import *


def add():
    y = int(input())
    z = int(input())
    x = y + z
    return x


def sub():
    y = int(input())
    z = int(input())
    x = y - z
    return x


def mult():
    y = int(input())
    z = int(input())
    x = y * z
    return x


def div():
    y = int(input())
    z = int(input())
    try:
        x = y / z
    except ZeroDivisionError:
        x = "Impossible"
    return x


def pot():
    y = int(input())
    z = int(input())
    x = y ** z
    return x


def raiz():
    y = int(input())
    z = int(input())
    x = y + z
    return x


inicio = Tk()                                   # estruturas básica
inicio.title("Calculadora")                     # colocar título

# tamanho do quadrado, largura por altura em string, o + indica o local onde ela aparece inicialmente
inicio.geometry("350x600+900+50")
# se pode redimensionar a janela, pode-se colocar 0 e 1
inicio.resizable(False, False)
# inicio.minsize("ZZZxZZZ") ou .maxsize("ZZZxZZZ") se o resizable for true, ele indica até
# o maximo de largura que você pode estender a tela
# .state("zoomed") abre o app em seu maxsize,("iconic") abre no minsize
# Coloca-se dessa forma para mudar a cor que deve ser em inglês
#inicio['bg'] = "Black"
inicio.iconbitmap("images/calculadora.ico")     # colocar ícone

botao = Button(inicio, text="Soma", command=add())
botao.pack()  # deve ter para ter o botão

inicio.mainloop()


def main():
    print()


if __name__ == "__main__":
    main()
