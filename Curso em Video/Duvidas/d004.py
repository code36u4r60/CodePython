matriz = []
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, []]
marcador = False
vitoria = False
referencia = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, []]]
num = 0
linha = 0
coluna = 0
c = 0
l = 0

import random


def main():
    gerar_matriz()
    while vitoria == False:
        trocar_numeros()
        verificar_vitoria()


def gerar_matriz():
    for li in range(1, 5):
        lista = []
        for co in range(1, 5):
            n = random.choice(numeros)
            lista.append(n)
            numeros.remove(n)
        matriz.append(lista)
    _print(matriz)


def trocar_numeros():
    global marcador, num, linha, coluna, c, l
    validar_jogada()

    matriz[l][c] = matriz[linha][coluna]
    matriz[linha][coluna] = []
    _print(matriz)


def validar_jogada():
    global marcador, num, linha, coluna, c, l
    marcador = False
    while marcador == False:
        num = int(input('Digite o valor a ser movimentado: '))
        for lista in matriz:
            for col in lista:
                if col == num:
                    linha = matriz.index(lista)
                    coluna = lista.index(col)
        for lista in matriz:
            for col in lista:
                if col == []:
                    l = matriz.index(lista)
                    c = lista.index(col)
        if linha == l and coluna == (c + 1):
            marcador = True
        elif linha == l and coluna == (c - 1):
            marcador = True
        elif linha == (l + 1) and coluna == c:
            marcador = True
        elif linha == (l - 1) and coluna == c:
            marcador = True
        else:
            print('Movimento inválido!')


def verificar_vitoria():
    global vitoria
    vitoria = False
    if matriz == referencia:
        vitoria = True
        print('Vitória!')
    else:
        vitoria = False


def _print(matrix):
    for i in range(0, 3):
        print('[', end='')
        for j in range(0, 4):
            print(' {:>2} '.format(str(matrix[i][j])), end='')
        print(']')


main()