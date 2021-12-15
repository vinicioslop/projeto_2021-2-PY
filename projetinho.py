# DEFINE E DIRECIONA AS OPÇÕES DE PÁGINAS
def paginas(pagina):
    pagina01 = """
+**************************************************+"
| █████████ Bem-vindo ao Projeto 2021/2! █████████ |"
| ████████████████ Python version ████████████████ |"
+==================================================+"
| Escolha uma das opções abaixo para realização de |"
| cálculos matemáticos.                            |"
+==================================================+"
| 1 - SOMA                                         |"
| 2 - SUBTRAÇÃO                                    |"
| 3 - MULTIPLICAÇÃO                                |"
| 4 - DIVISÃO                                      |"
| 5 - EXPONENCIAÇÃO                                |"
| 6 - RADICIAÇÃO                                   |"
| 7 - FATORIAL                                     |"
| 8 - MAIOR DIVISOR COMUM                          |"
| 9 - PRÓXIMA PÁGINA                               |"
| 0 - SAIR                                         |"
+--------------------------------------------------+"
| ██████████████████ PÁGINA 1/2 ██████████████████ |"
+==================================================+"
"""

    pagina02 = """
+**************************************************+"
| █████████ Bem-vindo ao Projeto 2021/2! █████████ |"
+==================================================+"
| Escolha uma das opções abaixo para realização de |"
| cálculos matemáticos.                            |"
+==================================================+"
| 1 - ESTIMA PI                                    |"
| 2 - ESTIMA EULER                                 |"
|                                                  |"
|                                                  |"
|                                                  |"
|                                                  |"
|                                                  |"
| 8 - SOBRE O PROJETO                              |"
| 9 - VOLTAR                                       |"
| 0 - SAIR                                         |"
+--------------------------------------------------+"
| ██████████████████ PÁGINA 2/2 ██████████████████ |"
+==================================================+"
"""

    if pagina == 1:
        return pagina01
    if pagina == 2:
        return pagina02
# FINAL DO DIRECIONAMENTO DE PÁGINAS

# LÓGICA DE PARADA
def EsperaTecla():
    input("Pressione qualquer tecla para continuar...")
# FINAL DA LÓGICA DE PARADA

# LÓGICA DE SOMA
def Somar():
    console

    barra = """
    +**************************************************+
    | ████████████████████ SOMA ██████████████████████ |
    +==================================================+
    """

    print(barra + "\n")

    valor01 = float(input("Informe o primeiro valor: "))
    valor02 = float(input("Informe o segundo valor: "))

    sum = valor01 + valor02

    print(str(valor01) + " + " + str(valor02) + " = " + str(sum))

    EsperaTecla()
# FINAL DA LÓGICA DE SOMA

# LÓGICA DE SUBTRAÇÃO
def Subtrair():
    barra = """
    +**************************************************+
    | ██████████████████ SUBTRAÇÃO ███████████████████ |
    +==================================================+
    """

    print(barra + "\n")

    valor01 = float(input("Informe o primeiro valor: "))
    valor02 = float(input("Informe o segundo valor: "))

    sub = valor01 - valor02

    print(str(valor01) + " - " + str(valor02) + " = " + str(sub))

    EsperaTecla()
# FINAL DA LÓGICA DE SUBTRAÇÃO

# LÓGICA DE MULTIPLICAÇÃO
def Multiplicar():
    barra = """
    +**************************************************+
    | ████████████████ MULTIPLICAÇÃO █████████████████ |
    +==================================================+
    """

    print(barra + "\n")

    valor01 = float(input("Informe o primeiro valor: "))
    valor02 = float(input("Informe o segundo valor: "))

    mult = valor01 * valor02

    print(str(valor01) + " x " + str(valor02) + " = " + str(mult))

    EsperaTecla()
# FINAL DA LÓGICA DE MULTIPLICAÇÃO

# LÓGICA DE DIVISÃO
def Dividir():
    barra = """
    +**************************************************+
    | ████████████████████ DIVISÃO ███████████████████ |
    +==================================================+
    """

    print(barra + "\n")

    valor01 = float(input("Informe o primeiro valor: "))
    valor02 = float(input("Informe o segundo valor: "))

    div = valor01 / valor02

    print(str(valor01) + " / " + str(valor02) + " = " + str(div))

    EsperaTecla()
# FINAL DA LÓGICA DE DIVISÃO

# LÓGICA DE EXPONENCIAÇÃO
def Exponenciacao():
    barra = """
    +**************************************************+
    | █████████████████ EXPONENCIAÇÃO ████████████████ |
    +==================================================+
    """

    print(barra + "\n")

    valorBase = float(input("Informe o valor da base....: "))
    valorExpoente = float(input("Informe o valor do expoente: "))

    potencia = valorBase ** valorExpoente

    print(str(valorBase) + " ^ " + str(valorExpoente) + " = " + str(potencia))

    EsperaTecla()
# FINAL DA LÓGICA DE EXPONENCIAÇÃO

# LÓGICA DE RADICIAÇÃO
def Radiciacao():
    barra = """
    +**************************************************+
    | █████████████████ RADICIAÇÃO ███████████████████ |
    +==================================================+
    """

    print(barra + "\n")

    radicando = float(input("Informe o radicando: "))
    indice = float(input("Informe o índice...: "))

    resultado = radicando ** (1 / indice)

    print("O resultado é " + str(resultado))

    EsperaTecla()
# FINAL DA LÓGICA DE RADICIAÇÃO

# LÓGICA DE FATORIAL
def calcFat(valor):
    fat = 1

    if valor == 0:
        return fat

    x = 2
    while x <= valor:
        fat *= x
        x += x

    return fat
def Fatorial():
    barra = """
    +**************************************************+
    | ███████████████████ FATORIAL ███████████████████ |
    +==================================================+
    """

    print(barra + "\n")

    entrada = int(input("Informe um valor inteiro: "))

    fat = calcFat(entrada)

    print(str(entrada) + "! = " + str(fat))

    EsperaTecla()
# FINAL DA LÓGICA DE FATORIAL

# LÓGICA DE MDC
def MDC():
    barra = """
    +**************************************************+
    | ███████ MÁXIMO DIVISOR COMUM (ITERATIVO) ███████ |
    +==================================================+
    """

    print(barra + "\n")

    valorA = float(input("Informe o 1º número (a): "))
    valorB = float(input("Informe o 2º número (b): "))

    r = -1

    while not valorB == 0:
        r = valorA % valorB
        valorA = valorB
        valorB = r

    mdc = valorA

    print("MDC (a, b) = " + str(mdc))

    EsperaTecla()
# FINAL DA LÓGICA DE MDC

# LÓGICA DE ESTIMA PI
def EstimaPI():
    barra = """
    +**************************************************+
    | ███████████████████ ESTIMA PI ██████████████████ |
    +==================================================+
    """

    print(barra + "\n")

    iteracoes = int(input("Quantas iteracões? "))

    if iteracoes < 1:
        print("Quantidade de iterações inválida! Precisa ser maior ou igual a 1.")
        EsperaTecla()
        return

    pi = 0
    aux = 3
    
    for i in range(iteracoes - 1):
        if i % 2 == 0:
            pi += 1 / aux
            aux += 2
        else:
            pi -= 1 / aux
            aux += 2

    pi = pi - 1
    pi = pi * 4
    pi = pi * (-1)

    print("Estimativa: " + str(pi))

    EsperaTecla()
# FIM DA LÓGICA DE ESTIMA PI

# LÓGICA DE ESTIMA EULER
def EstimaEuler():
    barra = """
    +**************************************************+"
    | ██████████████████ ESTIMA EULER ████████████████ |"
    +==================================================+
    """

    print(barra + "\n")

    iteracoes = int(input("Quantidade de iterações? "))

    if iteracoes < 1:
        print("Quantidade de iterações inválida! Precisa ser maior ou igual a 1.")
        EsperaTecla()
        return

    euler = 0
    
    for i in range(iteracoes):
        euler += 1.0 / calcFat(i)

    print("Estimativa: " + str(euler))

    EsperaTecla()
# FIM DA LÓGICA DE ESTIMA EULER

# LÓGICA DE NOTHING
def Nothing():
    print("There is nothing to see here, go away!!!")
    EsperaTecla()
# FIM DA LÓGICA DE NOTHING

# LÓGICA DE CRÉDITOS
def Creditos():
    creditos = """
     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   Projetinho realizado para finalização
    █────────▄▄▄▄▄▄────────█  do módulo de programação em .NET C#,
    █──────█▀──────▀█──────█  alternando em versões.
    █─────█─▄▀█──█▀▄─█─────█
    █────▐▌──────────▐▌────█  user: vinicioslop
    █────█▌▀▄──▄▄──▄▀▐█────█  link: https://vinicioslop.github.io/projeto_2021-2/
    █───▐██──▀▀──▀▀──██▌───█
    █──▄████▄──▐▌──▄████▄──█
     ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    """

    print(creditos + "\n")

    opcao = input("Sair do programa? (S)im ou (N)ão: ")

    if opcao.upper() == "S":
        print("Saindo...")
        return True

    return False

# FIM DA LÓGICA DE CRÉDITOS

# DIRECIONADOR DE OPERAÇÕES
def opcoes_pagina01(opcao):
    if opcao == 1:
        Somar()
    elif opcao == 2:
        Subtrair()
    elif opcao == 3:
        Multiplicar()
    elif opcao == 4:
        Dividir()
    elif opcao == 5:
        Exponenciacao()
    elif opcao == 6:
        Radiciacao()
    elif opcao == 7:
        Fatorial()
    elif opcao == 8:
        MDC()
    else:
        print("Opção inválida!")
        EsperaTecla()

def opcoes_pagina02(opcao):        
    if opcao == 1:
        EstimaPI()
    elif opcao == 2:
        EstimaEuler()
    elif opcao == 3:
        Nothing()
    elif opcao == 4:
        Nothing()
    elif opcao == 5:
        Nothing()
    elif opcao == 6:
        Nothing()
    elif opcao == 7:
        Nothing()
    elif opcao == 8:
        sair = Creditos()
    else:
        print("Opção inválida!")
        EsperaTecla()
    
    return sair
# FINAL DA LÓGICA DE DIRECIONAMENTO DE OPÇÕES

# LÓGICA "MAIN" DO PROGRAMA PYTHON
def start():
    pagina = 1
    opcao = -1
    sair = False

    while not sair:
        print(paginas(pagina))

        opcao = int(input("Opção desejada: "))

        if opcao == 0:
            print("Saindo...")
            break
        elif opcao > 0 and opcao < 9:
            if pagina == 1:
                opcoes_pagina01(opcao)
            elif pagina == 2:
                sair = opcoes_pagina02(opcao)
            else:
                print("Opção digitada é inválida")
        if opcao == 9:
            if pagina == 1:
                pagina = 2
            else:
                pagina = 1
# FINAL DA LÓGICA "MAIN"


# INICIA A EXECUÇÃO DO PROGRAMA
start()
