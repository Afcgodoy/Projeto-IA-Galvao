import os
import json
from PyPDF2 import PdfReader

#Pasta com os arquivos PDF a serem convertidos
pasta = "arquivos"

#Nome do arquivo JSON onde quero que o conteúdo convertido seja inserido
arquivo_json = 'cc2025.json'

# Lista para armazenar os dados no formato consulta-conteudo
dados = []

# Percorre todos os arquivos na pasta
for arquivo in os.listdir(pasta):
    print(f"arquivo {arquivo}...")
    if arquivo.lower().endswith(".pdf"):
        caminho_pdf = os.path.join(pasta, arquivo)
        
        # Extrai o texto do PDF
        texto = ""
        try:
            with open(caminho_pdf, "rb") as f:
                reader = PdfReader(f)
                for page in reader.pages:
                    texto += page.extract_text()
        except Exception as e:
            texto = f"Erro ao extrair texto: {str(e)}"
        
        # Adicionar o conteúdo no formato desejado à lista/dicionário
        dados.append({
            "consulta": arquivo,
            "conteudo": texto.strip()
        })

# Salva os dados em um arquivo JSON
with open(arquivo_json, "w", encoding="utf-8") as json_file:
    json.dump(dados, json_file, ensure_ascii=False, indent=4)


print("Arquivo JSON criado com sucesso!")
