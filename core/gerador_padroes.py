def gerar_padroes(tam_barra, tam_cortes):
    qtd_tipos_corte = len(tam_cortes)
    padroes = []

    def gerar_combinacoes(index, padrao_atual, espaco_restante):
        if index == qtd_tipos_corte:
            if sum(padrao_atual) > 0:
                padroes.append(padrao_atual[:])
            return

        tamanho_item_atual = tam_cortes[index]
        max_itens_atual = espaco_restante // tamanho_item_atual

        for qtd in range(max_itens_atual + 1):
            padrao_atual[index] = qtd

            novo_espaco = espaco_restante - (qtd * tamanho_item_atual)

            gerar_combinacoes(index + 1, padrao_atual, novo_espaco)

            padrao_atual[index] = 0

    padrao_inicial = [0] * qtd_tipos_corte
    gerar_combinacoes(0, padrao_inicial, tam_barra)

    return padroes

