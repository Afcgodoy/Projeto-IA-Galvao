import undetected_chromedriver as uc
import time

chrome_options = uc.ChromeOptions()

chrome_options.add_experimental_option('prefs', {
    "download.default_directory": r"C:\Users\AnaFláviaGodoy\Desktop\Acordaos\acordaos",
    "download.directory_upgrade": True,
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True,
    "safebrowsing.enabled": True,
})

def listarErros(link, arquivo='erros.txt'):
    with open(arquivo, 'a') as arq:
        arq.write(f"{link}\n")
        
navegador = uc.Chrome(options = chrome_options)

with open('links.txt', 'r') as arq:
    links = arq.read().splitlines()

i=0
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
    
    
    
