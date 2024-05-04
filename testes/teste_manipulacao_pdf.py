import fitz # type: ignore
from pprint import pprint

pdf = fitz.open("arquivos/pdf_teste.pdf") 
pagina = pdf[0] 
linhas = pagina.find_tables()[0].extract()

print(linhas[2][2])

#if tabela.tables:  
#   pprint(tabela[0].extract()) 