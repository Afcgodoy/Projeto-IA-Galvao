import json

with open('arquivos_entrada.txt', 'r') as file:
    entradas = file.read().splitlines()
    
with open('arquivos_saida.txt', 'r') as file:
    saidas = file.read().splitlines()
    
    
for entrada,saida in zip(entradas, saidas):
    
    dados = []
    
    with open(entrada, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue  # ignora linhas vazias
            try:
                # Converte a linha para dicionário
                item = json.loads(linha)
                # Cria novo formato
                
                conteudo_limpo = item.get("text", "").replace('"', '')
                
                
                novo_item = {
                    "artigo": item.get("title", ""),
                    "conteudo": conteudo_limpo
                }
                dados.append(novo_item)
            except json.JSONDecodeError as e:
                print(f"Erro ao processar linha: {e}")
                
    # Salva o JSON final
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    print(f"✅ Arquivo JSON criado com sucesso: {saida}")