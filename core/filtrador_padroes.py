def filtrar_padroes(padroes, cortes, tam_barra):
    menor_corte = min(cortes)
    padroes_validos = []

    for padrao in padroes:
        total_usado = sum(p * c for p, c in zip(padrao, cortes))
        sobra = tam_barra - total_usado

        if sobra < menor_corte:
            padroes_validos.append(padrao)

    return padroes_validos

