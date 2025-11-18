from ortools.linear_solver import pywraplp 
from core.gerador_padroes import gerar_padroes as gp
from core.filtrador_padroes import filtrar_padroes as fp

def main():
    tam_barra = 150
    tam_cortes = [80, 60, 50]

    print(f"--- Configuração ---")
    print(f"Tamanho da Barra: {tam_barra}")
    print(f"Demandas de Corte: {tam_cortes}\n")

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
    
