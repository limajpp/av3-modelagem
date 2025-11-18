def ler_dados_entrada(caminho_arquivo):
    info = {
        "tam_barra": 0,
        "qtd_tipos": 0,
        "itens": [] 
    }

    try:
        with open(caminho_arquivo, "r") as arquivo:
            cabecalho = arquivo.readline().split()
            if not cabecalho:
                raise ValueError("Arquivo está vazio...")
            
            info["tam_barra"] = int(cabecalho[0])
            info["qtd_tipos"] = int(cabecalho[1])

            for linha in arquivo:
                dados = linha.split()
                if len(dados) > 2:
                    raise ValueError("O arquivo contém informações de cortes e demandas inválidas...")
                else:
                    item = {
                        "tamanho": int(dados[0]),
                        "demanda": int(dados[1])
                    }
                    info["itens"].append(item)
                    
        return info

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado...")
        return None
    except ValueError:
        print("Erro: O arquivo contém dados inválidos (não numéricos)...")
        return None

dados_lidos = ler_dados_entrada("test/example.txt")

