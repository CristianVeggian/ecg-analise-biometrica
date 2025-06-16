# ecg-analise-biometrica

Este repositório contém os arquivos, scripts e dataset utilizados no desenvolvimento do trabalho **"Mineração de Padrões Biométricos e Demográficos em Sinais de ECG: Um Estudo com Algoritmos de Clusterização e Classificação"**, desenvolvido no contexto da disciplina de Data Mining do Programa de Pós-Graduação em Engenharia Elétrica e Informática Industrial (CPGEI) da Universidade Tecnológica Federal do Paraná (UTFPR), durante o primeiro semestre de 2025.

## 📂 Estrutura do Repositório

📁 datasets/ → Conjunto de dados brutos e processados
📁 scripts/ → Scripts Python para pré-processamento e extração de características
📁 orange/ → Arquivos .ows com fluxos do Orange (clusterização e classificação)
📄 README.md → Este arquivo

## ⚙️ Tecnologias utilizadas

- Python 3.10+
  - numpy
  - scipy
  - biosppy
  - tsfel
  - pandas
- Orange Data Mining
- LaTeX (para documentação e artigo)

## 📑 Descrição do Projeto

O objetivo deste projeto foi investigar a viabilidade de utilizar sinais de ECG como fonte de identificação biométrica e caracterização demográfica, explorando técnicas de extração de características, clusterização e classificação supervisionada. Foram analisados atributos como idade, sexo, peso, altura e tipo sanguíneo.

## 📁 Dataset

Os dados foram coletados com hardware baseado no módulo AD8232, ESP32 e eletrodos Ag/AgCl. As informações pessoais dos participantes foram anonimizadas, sendo mantidos apenas identificadores numéricos e metadados relevantes para as análises.

**IMPORTANTE:** O dataset completo está disponível apenas para fins acadêmicos e está sujeito às restrições éticas da instituição.

## ▶️ Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/ecg-analise-biometrica.git
```

Execute o script Python 'features.py' dentro da pasta /scripts para gerar os arquivos de características.

Abra os arquivos .ows na interface do Orange para reproduzir os experimentos de clusterização e classificação.

📜 Licença
Este projeto está licenciado sob a licença MIT — consulte o arquivo LICENSE para mais detalhes.

📧 Contato
Cristian Veggian Matias
cristianveggian@gmail.com
Lattes: http://lattes.cnpq.br/4453425163468096
Orcid: https://orcid.org/0009-0008-1281-3099
