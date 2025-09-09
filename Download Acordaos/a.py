def a(dado, arquivo='links.txt'):
    with open(arquivo, 'a') as arq:
        arq.write(f"{dado}\n")
        
for i in range(603000, 1000000):
    i_str = str(i)
    texto = "https://www6.fazenda.mg.gov.br/sifweb/ExibeDocumento?caminho=/usr/sef/sifweb/www2/secretaria/conselho_contribuintes/acordaos/" + i_str + "ce.pdf"
    a(texto)