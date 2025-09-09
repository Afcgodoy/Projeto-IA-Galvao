import json

# Caminho do arquivo TXT de entrada
arquivo_txt = "new_wiki_00.txt"

# Caminho do JSON de saída
arquivo_json = "saida.json"

dados = []

with open(arquivo_txt, "r", encoding="utf-8") as f:
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
with open(arquivo_json, "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print(f"✅ Arquivo JSON criado com sucesso: {arquivo_json}")
