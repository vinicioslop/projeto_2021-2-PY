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
def espera_tecla():
    input("Pressione qualquer tecla para continuar...")
# FINAL DA LÓGICA DE PARADA

# LÓGICA DE SOMA
def Somar():
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

    espera_tecla()
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

    espera_tecla()
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

    espera_tecla()
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

    espera_tecla()
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

    espera_tecla()
# FINAL DA LÓGICA DE EXPONENCIAÇÃO

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
        print("  Opção inválida!")
        EsperaTecla()

def opcoes_pagina02(opcao):
    if opcao == 1:
        soma()
    elif opcao == 2:
        sub()
    elif opcao == 3:
        mult()
    elif opcao == 4:
        div()
# FINAL DA LÓGICA DE DIRECIONAMENTO DE OPÇÕES

# LÓGICA "MAIN" DO PROGRAMA PYTHON
def start():
    pagina = 1
    opcao = -1

    while True:
        print(paginas(pagina))

        opcao = int(input("Opção desejada: "))

        if opcao == 0:
            print("Saindo...")
            break
        elif opcao > 0 and opcao < 9:
            if pagina == 1:
                opcoes_pagina01(opcao)
            elif pagina == 2:
                opcoes_pagina02(opcao)
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
