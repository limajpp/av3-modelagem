from ortools.linear_solver import pywraplp

def resolver_problema_corte(tam_barra, padroes, tam_cortes, demandas):
    solver = pywraplp.Solver.CreateSolver('SCIP')

    if not solver:
        return None

    num_padroes = len(padroes)
    num_itens = len(tam_cortes)

    limite_superior = sum(demandas)

    variaveis = []
    for j in range(num_padroes):
        variaveis.append(solver.IntVar(0, limite_superior, f'x{j+1}'))

    desperdicios = []
    for padrao in padroes:
        total_usado = sum(padrao[i] * tam_cortes[i] for i in range(num_itens))
        desperdicio = tam_barra - total_usado
        desperdicios.append(desperdicio)

    objetivo = solver.Objective()
    for j in range(num_padroes):
        objetivo.SetCoefficient(variaveis[j], 1)
    objetivo.SetMinimization()

    for i in range(num_itens):
        restricao = solver.Constraint(demandas[i], solver.infinity())
        for j in range(num_padroes):
            restricao.SetCoefficient(variaveis[j], padroes[j][i])

    status = solver.Solve()

    resultado = {
        'status': status,
        'padroes': padroes,
        'desperdicios': desperdicios,
        'variaveis': variaveis,
        'solver': solver,
        'num_itens': num_itens,
        'demandas': demandas,
        'tam_cortes': tam_cortes,
        'tam_barra': tam_barra
    }

    return resultado

def exibir_modelo(resultado):
    padroes = resultado['padroes']
    desperdicios = resultado['desperdicios']
    variaveis = resultado['variaveis']
    num_itens = resultado['num_itens']
    demandas = resultado['demandas']
    tam_cortes = resultado['tam_cortes']

    print("\n--- MODELO DE PROGRAMACAO LINEAR INTEIRA ---\n")

    print("Minimizar:")
    termos_fo = []
    for j in range(len(padroes)):
        termos_fo.append(f"x{j+1}")
    print("  " + " + ".join(termos_fo))

    print("\nSujeito a:")
    for i in range(num_itens):
        termos = []
        for j in range(len(padroes)):
            coef = padroes[j][i]
            if coef > 0:
                termos.append(f"{coef}x{j+1}")
        if termos:
            print(f"  {' + '.join(termos)} >= {demandas[i]}")

    print(f"\n  x1, ..., x{len(padroes)} >= 0 e inteiras")

    print("\n--- TIPO DO PROBLEMA ---")
    print("PLI (Programacao Linear Inteira)")

def exibir_solucao(resultado):
    status = resultado['status']
    solver = resultado['solver']
    variaveis = resultado['variaveis']
    padroes = resultado['padroes']
    desperdicios = resultado['desperdicios']
    tam_barra = resultado['tam_barra']
    tam_cortes = resultado['tam_cortes']

    if status == pywraplp.Solver.OPTIMAL:
        print("\n--- SOLUCAO OTIMA ENCONTRADA ---\n")

        print("Padroes utilizados:")
        total_barras = 0
        total_desperdicio = 0

        for j in range(len(variaveis)):
            valor = int(variaveis[j].solution_value())
            if valor > 0:
                padrao = padroes[j]
                desperdicio_unitario = desperdicios[j]

                print(f"  Padrao {j+1}: {padrao}")
                print(f"    Quantidade: {valor} barras")
                print(f"    Desperdicio por barra: {desperdicio_unitario}m")
                print(f"    Desperdicio total: {valor * desperdicio_unitario}m")

                composicao = []
                for i in range(len(padrao)):
                    if padrao[i] > 0:
                        composicao.append(f"{padrao[i]}x{tam_cortes[i]}m")
                print(f"    Composicao: {' + '.join(composicao)}")
                print()

                total_barras += valor
                total_desperdicio += valor * desperdicio_unitario

        print(f"Total de barras utilizadas: {total_barras}")
        print(f"Desperdicio total: {total_desperdicio}m")
        print(f"Valor da funcao objetivo: {solver.Objective().Value()}")

    elif status == pywraplp.Solver.FEASIBLE:
        print("\nSolucao viavel encontrada (nao otima).")
    else:
        print("\nNenhuma solucao encontrada.")
