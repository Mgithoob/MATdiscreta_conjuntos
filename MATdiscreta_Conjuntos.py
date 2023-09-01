# Miguel Augusto Cardoso Dambroski, Rogério Vinicius Grzbowski Ferreira

def operacao(operacao, conjunto1, conjunto2):

    if operacao == 'U':
        op_string = 'União'
        conjunto_resultado = conjunto1 | conjunto2

    elif operacao == 'I':
        op_string = 'Intersecção'
        conjunto_resultado = conjunto1 & conjunto2

    elif operacao == 'D':
        op_string = 'Diferença'
        conjunto_resultado = conjunto1 - conjunto2

    elif operacao == 'C':
        op_string = 'Produto Cartesiano'
        conjunto_resultado = {(a, b) for a in tuple(conjunto1) for b in list(conjunto2)}

    else:
        op_string = 'Inválida'
        conjunto_resultado = 'ERRO'

    return conjunto_resultado, op_string


def converter_set(string):

    for i in range(len(string)):
        numeros_strings = string.split(', ')
        i += 1
    conjunto_resultado = set(numeros_strings)

    return conjunto_resultado


dados = open("teste_2.txt", "r")
count = 0
loop = True

while loop:
    count += 1

    # Checa o id de qtde de operações
    if count == 1:
        qtde_op = int(dados.readline())
        qtdelinhas = (qtde_op * 3 + 1)
        opcount = 2

        if qtde_op < 1:
            print('Não há operações a serem feitas!')
            loop = False
    # Termina quando não há mais linhas pra ler.
    elif count > qtdelinhas:
        loop = False

    # Checa o id da operação
    elif count == opcount:
        op_atual_linha = opcount
        opcount += 3
        op_atual = (dados.readline()).strip()

    # Recebe primeiro conjunto da operação
    elif count == (op_atual_linha + 1):
        conjunto1 = (dados.readline()).strip()
        if conjunto1 == '':
            conjunto1_set = set()
        else:
            conjunto1_set = converter_set(conjunto1)

    # Recebe segundo conjunto da operação, faz operação e mostra o resultado.
    elif count == (op_atual_linha + 2):
        conjunto2 = (dados.readline()).strip()
        if conjunto2 == '':
            conjunto2_set = set()
        else:
            conjunto2_set = converter_set(conjunto2)

        Resultado, Tipo = operacao(op_atual, conjunto1_set, conjunto2_set)

        # sets vazios printam como {∅}
        if not conjunto1_set:
            conjunto1_set_str = '{∅}'
        else:
            conjunto1_set_str = str(conjunto1_set)
        if not conjunto2_set:
            conjunto2_set_str = '{∅}'
        else:
            conjunto2_set_str = str(conjunto2_set)
        if not Resultado:
            Resultado_str = '{∅}'
        else:
            Resultado_str = str(Resultado)

        print("{}: Conjunto 1 {}, conjunto 2 {}. Resultado: {}".format(Tipo, conjunto1_set_str, conjunto2_set_str, Resultado_str))

dados.close()
