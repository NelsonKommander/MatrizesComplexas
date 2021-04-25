import os
import numpy as np

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def obter_caminho():
    print("Forneca o caminho da imagem:")
    return str(input())

def validar_caminho(caminho):
    arquivoExiste = os.path.isfile(caminho)
    return arquivoExiste

def main():
    clear()

    print("Bem vindo ao resolvedor de prova de eletrica 5000")
    print("=================================================")

    caminho = obter_caminho()
    valido = validar_caminho(caminho)

    while valido == False:
        print("Caminho inválido, por favor forneca um caminho válido ou envie 'q' para sair")
        caminho = obter_caminho()

        if caminho == "q":
            return

        valido = validar_caminho(caminho)

    arquivoDeEntrada = open(caminho)

    ordem = int(arquivoDeEntrada.readline())

    coeficientes = []
    resposta = []

    for m in range(ordem):
        linha = arquivoDeEntrada.readline().split(' ')
        vetor = []

        for i in range(ordem):
            vetor.append(float(linha[i]))

        coeficientes.append(vetor)
        resposta.append(float(linha[ordem]))

    arquivoDeEntrada.close()

    sol = np.linalg.solve(coeficientes, resposta)

    print("Solucao do seu sistema é: ", sol)


main()
#teste_matriz()