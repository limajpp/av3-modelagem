from core.gerador_padroes import gerar_padroes as gp
from core.filtrador_padroes import filtrar_padroes as fp
from core.solver import resolver_problema_corte, exibir_modelo, exibir_solucao
from utils.txt_input_reader import dados_lidos as data

def main():
    tam_barra = data["tam_barra"]
    tam_cortes = [item["tamanho"] for item in data["itens"]]
    demandas = [item["demanda"] for item in data["itens"]]

    print("=" * 60)
    print("PROBLEMA DE CORTE UNIDIMENSIONAL")
    print("=" * 60)

    print(f"\n--- CONFIGURACAO DO PROBLEMA ---\n")
    print(f"Tamanho da Barra: {tam_barra}m")
    print(f"Quantidade de Tipos de Itens: {len(tam_cortes)}")
    print(f"\nItens a serem cortados:")
    for i, (tamanho, demanda) in enumerate(zip(tam_cortes, demandas), 1):
        print(f"  Item {i}: Tamanho = {tamanho}m, Demanda = {demanda} unidades")

    print(f"\n--- GERACAO DE PADROES ---\n")
    padroes_brutos = gp(tam_barra, tam_cortes)
    print(f"Total de padroes brutos gerados: {len(padroes_brutos)}")

    print(f"\n--- FILTRAGEM DE PADROES ---\n")
    padroes_finais = fp(padroes_brutos, tam_cortes, tam_barra)
    print(f"Total de padroes validos: {len(padroes_finais)}")

    print(f"\nPadroes validos para o problema:")
    for idx, padrao in enumerate(padroes_finais, 1):
        total_usado = sum(padrao[i] * tam_cortes[i] for i in range(len(tam_cortes)))
        desperdicio = tam_barra - total_usado
        composicao = []
        for i in range(len(padrao)):
            if padrao[i] > 0:
                composicao.append(f"{padrao[i]}x{tam_cortes[i]}m")
        print(f"  p{idx}: {' + '.join(composicao)} (desperdicio = {desperdicio}m)")

    print(f"\n--- RESOLVENDO COM OR-TOOLS ---\n")
    resultado = resolver_problema_corte(tam_barra, padroes_finais, tam_cortes, demandas)

    if resultado:
        exibir_modelo(resultado)
        exibir_solucao(resultado)
    else:
        print("Erro ao criar o solver.")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
    
