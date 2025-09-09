Download Acórdãos
---
Esse programa tem o objetivo de baixar todos os acórdãos da legislação tributária mineira.
Funciona do seguinte modo:

O diretório possui uma lista de todos os links possíveis para os acórdãos (os acórdãos tem uma numeração padrão de 6 dígitos, então criei links para todas as possibilidades usando excel), que estão no arquivo 'links.txt'.

O programa irá buscar todos os links possíveis no google, e devido a configuração do driver, caso o link leve a um arquivo pdf, ele irá baixar o arquivo diretamente no diretório configurado, sem fazer nenhuma solicitação ao usuário. Caso não tenha sido realizado um download, o link será escrito em um arquivo chamado 'erros.txt'.

Biblioteca usada: 'undetected_chromedriver'

(É necessário que o google Chrome da sua máquina esteja na versão mais recente para que a biblioteca rode)

