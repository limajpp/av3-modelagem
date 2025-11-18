from ortools.linear_solver import pywraplp 
from core.gerador_padroes import gerar_padroes as gp
from core.filtrador_padroes import filtrar_padroes as fp
from utils.txt_input_reader import dados_lidos as data

def main():
    tam_barra = data["tam_barra"]
    tam_cortes = [item["tamanho"] for item in data["itens"]]
    demandas = [item["demanda"] for item in data["itens"]]
    
    print(f"--- Configuração ---")
    print(f"Tamanho da Barra: {tam_barra}")
    print(f"Tamanhos de Corte: {tam_cortes}")
    print(f"Demandas: {demandas}\n")

    print("Gerando padrões possíveis...")
    padroes_brutos = gp(tam_barra, tam_cortes)
    print(f"Total de padrões gerados: {len(padroes_brutos)}")
    for pb in padroes_brutos:
        print(pb)
    
    print("Filtrando padrões ineficientes...")
    padroes_finais = fp(padroes_brutos, tam_cortes, tam_barra)
    
    print(f"Padrões Válidos Finais: {len(padroes_finais)}")
    for pf in padroes_finais:
        print(pf)

if __name__ == "__main__":
    main()
    
