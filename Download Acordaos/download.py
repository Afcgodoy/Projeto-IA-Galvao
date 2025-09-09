import undetected_chromedriver as uc
import time

chrome_options = uc.ChromeOptions()

#Definindo as configurações do driver

chrome_options.add_experimental_option('prefs', {
    "download.default_directory": r"C:\Users\AnaFláviaGodoy\Desktop\Acordaos\acordaos", #Definindo o diretório onde os arquivos devem ser baixados
    "download.directory_upgrade": True, #Para atualizar o diretório onde os arquivos serão baixados
    "download.prompt_for_download": False, #Para que não seja necessária uma ação do usuário para o início do download
    "plugins.always_open_pdf_externally": True, #Para que o navegador não fique abrindo todos os PDFs que forem baixados
    "safebrowsing.enabled": True,
})

#Função para escrever no arquivo 'erros.txt' os links que tiveram erros no carregamento
def listarErros(link, arquivo='erros.txt'):
    with open(arquivo, 'a') as arq:
        arq.write(f"{link}\n")
        
navegador = uc.Chrome(options = chrome_options)

#Para ler os links a serem consultados
with open('links.txt', 'r') as arq:
    links = arq.read().splitlines()

i=0

#Loop para consultar todos os links
for link in links:
    try:
        navegador.get(link)
        time.sleep(1)
    except:
        print("HOUVE UM ERRO")
        listarErros(link)

    i=i+1
    print(f"Link {i} consultado...\n")
    
print("Fim do processo.")
    
    
    
