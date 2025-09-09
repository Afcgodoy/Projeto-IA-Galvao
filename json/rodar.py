import os
import json
from PyPDF2 import PdfReader

# Nota: Certifique-se de instalar a biblioteca PyPDF2 com 'pip install PyPDF2' se não estiver instalada.

# Caminho da pasta com os PDFs
pasta = "2024"

# Lista para armazenar os dados no formato pergunta-resposta
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
                    texto += page.extract_text() + "\n"  # Adiciona uma nova linha entre páginas
        except Exception as e:
            texto = f"Erro ao extrair texto: {str(e)}"
        
        # Adiciona ao dicionário
        dados.append({
            "pergunta": arquivo,
            "resposta": texto.strip()  # Remove espaços extras no final
        })

# Salva os dados em um arquivo JSON
with open("cc2024.json", "w", encoding="utf-8") as json_file:
    json.dump(dados, json_file, ensure_ascii=False, indent=4)

print("Arquivo JSON criado com sucesso!")