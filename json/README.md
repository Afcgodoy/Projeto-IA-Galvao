Converter arquivo PDF para JSON
---
Esse programa foi feito para converter arquivos PDF de Consultas de COntribuinte para JSON, no formato consulta-conteudo.

O programa le o conteudo de cada arquivo PDF que está na pasta indicada, extrai seu conteúdo e adiciona aquela consulta a um dicionário. O nome do arquivo se torna o conteúdo do campo 'consulta' e o conteúdo do arquivo se torna o do campo 'conteudo'.

Após adicionar todas as consultas ao dicionário, ele será convertido em um arquivo JSON.

Biblioteca a ser baixada: PyPDF2. 
