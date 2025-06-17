import pandas as pd
import re
from os.path import join

arquivo_txt = join('datasets','meta.txt')

dados = []

with open(arquivo_txt, 'r', encoding='utf-8') as f:
    linhas = [linha.strip() for linha in f if linha.strip()]

for i in range(0, len(linhas), 7):
    bloco = linhas[i:i+7]
    if len(bloco) < 7:
        continue 

    nome = bloco[0]
    sexo = bloco[1]
    tipo_sang = bloco[2]

    altura = float(re.sub(r'[^\d,\.]', '', bloco[3]).replace(',', '.'))

    peso = float(re.sub(r'[^\d,\.]', '', bloco[4]).replace(',', '.'))

    idade = int(re.search(r'\d+', bloco[5]).group())

    condicoes = bloco[6]

    id = int(i/7)+1

    dados.append({
        'ID': id,
        'Sexo': sexo,
        'Tipo Sanguineo': tipo_sang,
        'Altura': altura,
        'Peso': peso,
        'Idade': idade,
        'Condições': condicoes,
    })

df = pd.DataFrame(dados)
df.to_csv(join('datasets','processed_data','metadados.csv'), index=False, encoding='utf-8')

print("Arquivo 'metadados.csv' gerado com sucesso!")
