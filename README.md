# ECG – Análise Biométrica e Demográfica

Este repositório contém os arquivos, scripts, dados processados e workflows utilizados no desenvolvimento do trabalho **"Mineração de Padrões Biométricos e Demográficos em Sinais de ECG: Um Estudo com Algoritmos de Clusterização e Classificação"**, desenvolvido no contexto da disciplina de Data Mining do Programa de Pós-Graduação em Engenharia Elétrica e Informática Industrial (CPGEI) da Universidade Tecnológica Federal do Paraná (UTFPR).

O projeto investiga a presença de informações biométricas e demográficas em características extraídas de sinais eletrocardiográficos (ECG), utilizando técnicas de aprendizado de máquina supervisionado e não supervisionado.

---

## 📑 Descrição do Projeto

O objetivo deste projeto é investigar a viabilidade da utilização de características derivadas de sinais de ECG para identificação biométrica e caracterização demográfica.

Os sinais foram adquiridos em condições de repouso e pós-atividade física e posteriormente submetidos a etapas de pré-processamento, segmentação dos ciclos cardíacos e extração de características.

Foram investigados os seguintes atributos:

- identificação do participante (`ID`);
- sexo;
- idade;
- peso;
- altura;
- tipo sanguíneo;
- estado de aquisição do sinal (repouso ou pós-atividade).

As análises foram realizadas utilizando técnicas de classificação, regressão e clusterização.

Para os atributos demográficos, a avaliação supervisionada utiliza separação independente por participante (*subject-wise validation*), de forma que segmentos de ECG pertencentes ao mesmo indivíduo não sejam simultaneamente utilizados nos conjuntos de treinamento e teste.

A identificação biométrica por `ID` é tratada separadamente como um problema de identificação *closed-set*. Nesse caso, utiliza-se validação cruzada estratificada, uma vez que as identidades avaliadas no conjunto de teste também precisam estar representadas durante o treinamento.

---

## 📂 Estrutura do Repositório

```text
ecg-analise-biometrica/
│
├── datasets/
│   ├── processed_data/
│   │   └── features.csv
│   ├── raw_data/
│   └── meta.txt
│
├── scripts/
│   └── scripts utilizados no processamento e extração de características
│
├── orange/
│   └── workflows (.ows) utilizados nos experimentos
│
├── README.md
└── LICENSE
```

### Principais diretórios

- `datasets/processed_data/` → dados processados utilizados nas análises, incluindo o arquivo `features.csv`;
- `datasets/raw_data/` → dados de ECG utilizados no processamento;
- `datasets/meta.txt` → metadados associados aos participantes;
- `scripts/` → scripts Python utilizados no processamento e extração de características;
- `orange/` → workflows `.ows` utilizados no Orange Data Mining para classificação, regressão e clusterização.

---

## 📁 Dataset

Os sinais de ECG foram adquiridos utilizando um sistema baseado no módulo **AD8232**, um microcontrolador **ESP32** e eletrodos **Ag/AgCl**.

As informações dos participantes utilizadas nas análises foram associadas a identificadores numéricos, permitindo relacionar os segmentos de ECG aos respectivos metadados durante os experimentos.

O arquivo principal utilizado nas análises de aprendizado de máquina é:

```text
datasets/processed_data/features.csv
```

Cada linha do arquivo representa um segmento de ECG processado e contém as características extraídas do sinal.

As primeiras colunas incluem:

- `ID` → identificador numérico do participante;
- `Estado` → condição de aquisição do sinal, correspondente a repouso ou pós-atividade.

As demais colunas correspondem às características extraídas dos sinais de ECG.

> **Nota:** no artigo e nos workflows de análise, `Estado` corresponde ao atributo denominado *Recording State* ou *State*.

### Considerações éticas

Os dados deste projeto foram obtidos em contexto acadêmico e devem ser utilizados considerando as condições e restrições éticas aplicáveis ao estudo.

O conjunto possui **26 participantes** e deve ser interpretado como uma base de dados de caráter exploratório. Os resultados obtidos não devem ser considerados evidência de generalização para populações clínicas ou comerciais.

---

## 📊 Características Extraídas

O arquivo `features.csv` contém o conjunto completo de características utilizadas nas análises.

Além das características extraídas automaticamente, foram calculadas separadamente seis características morfológicas relacionadas ao complexo QRS:

| Feature | Descrição |
|---|---|
| `R_amplitude` | Amplitude da onda R |
| `S_amplitude` | Amplitude da onda S |
| `RS_ratio` | Razão entre a amplitude de R e o valor absoluto da amplitude de S |
| `QRS_duration_s` | Duração do complexo QRS em segundos |
| `Slope_RS` | Inclinação entre os pontos R e S |
| `Area_QRS` | Área do complexo QRS |

As demais características foram extraídas automaticamente utilizando a biblioteca **TSFEL (Time Series Feature Extraction Library)**.

O conjunto inclui descritores pertencentes a diferentes domínios, incluindo:

- estatísticos;
- temporais;
- espectrais;
- cepstrais, incluindo MFCC e LPCC;
- baseados em espectrograma;
- baseados em transformadas wavelet.

Entre as características presentes no arquivo estão, por exemplo:

- Absolute Energy;
- Area Under the Curve;
- Autocorrelation;
- Average Power;
- Entropy;
- Interquartile Range;
- Kurtosis;
- Mean;
- Median;
- Standard Deviation;
- Variance;
- Root Mean Square;
- Skewness;
- Zero Crossing Rate;
- Fundamental Frequency;
- Median Frequency;
- Maximum Frequency;
- Spectral Centroid;
- Spectral Entropy;
- Spectral Kurtosis;
- Spectral Roll-off;
- Spectral Roll-on;
- Spectral Skewness;
- Spectral Spread;
- MFCC coefficients;
- LPCC coefficients;
- Spectrogram Mean Coefficients;
- Wavelet Energy;
- Wavelet Entropy;
- Wavelet Absolute Mean;
- Wavelet Standard Deviation;
- Wavelet Variance.

A **lista completa das características** pode ser consultada diretamente no cabeçalho do arquivo:

```text
datasets/processed_data/features.csv
```

As características extraídas automaticamente seguem as definições e implementações fornecidas pela biblioteca TSFEL. As características morfológicas adicionais relacionadas ao complexo QRS foram calculadas separadamente pelo pipeline desenvolvido para este projeto.

---

## 🧠 Aprendizado de Máquina

O projeto utiliza métodos de aprendizado de máquina supervisionado e não supervisionado.

### Classificação

Os algoritmos avaliados incluem:

- k-Nearest Neighbors (kNN);
- Naive Bayes;
- Random Forest;
- Multilayer Perceptron (MLP).

Os experimentos incluem identificação do participante e classificação de atributos biométricos e demográficos.

Para os atributos demográficos, os experimentos revisados utilizam validação independente por participante (*subject-wise validation*).

Para identificação por `ID`, utiliza-se validação cruzada estratificada em um cenário de identificação *closed-set*.

### Regressão

Também foram realizados experimentos de regressão para estimativa das seguintes variáveis contínuas:

- idade;
- altura;
- peso.

Esses experimentos também utilizam separação independente por participante.

### Aprendizado Não Supervisionado

Os algoritmos de clusterização avaliados incluem:

- k-means;
- DBSCAN;
- Hierarchical Clustering.

As análises de clusterização foram utilizadas de forma exploratória para investigar a existência de agrupamentos naturais no espaço de características derivadas do ECG.

Também foram utilizadas técnicas de visualização e avaliação, incluindo:

- t-SNE;
- Silhouette Analysis;
- dendrogramas para Hierarchical Clustering.

---

## 🧪 Validação por Participante

Como múltiplos segmentos de ECG são extraídos de um mesmo participante, uma divisão aleatória em nível de segmento pode colocar dados do mesmo indivíduo simultaneamente nos conjuntos de treinamento e teste.

Para reduzir esse efeito, os experimentos de predição demográfica utilizam separação por participante.

Em termos gerais:

```text
Participante A ─┐
Participante B ─┼── Treinamento
Participante C ─┘

Participante D ──── Teste
```

Dessa forma, todos os segmentos pertencentes a um participante permanecem no mesmo grupo durante a validação.

A identificação biométrica por `ID` constitui uma exceção, pois se trata de um problema *closed-set*. Nesse cenário, as identidades avaliadas durante o teste precisam estar representadas durante o treinamento, sendo utilizada validação cruzada estratificada.

---

## ⚙️ Tecnologias Utilizadas

### Python

O processamento dos sinais e a extração de características foram desenvolvidos utilizando Python 3.10+ e bibliotecas como:

- NumPy;
- SciPy;
- Pandas;
- BioSPPy;
- TSFEL;
- scikit-learn.

### Orange Data Mining

O **Orange Data Mining** foi utilizado para construção e execução dos workflows relacionados a:

- classificação;
- regressão;
- clusterização;
- validação dos modelos;
- análise de silhouette;
- visualização dos resultados.

Os workflows correspondentes estão disponíveis na pasta:

```text
orange/
```

### Outras ferramentas

- LaTeX → elaboração do artigo científico;
- Matplotlib → geração de visualizações complementares.

---

## ▶️ Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/CristianVeggian/ecg-analise-biometrica.git
cd ecg-analise-biometrica
```

### 2. Processamento e extração de características

Os scripts utilizados no processamento e na extração das características estão disponíveis na pasta:

```text
scripts/
```

O script responsável pela geração das características pode ser executado a partir dessa pasta conforme a organização atual do projeto.

O resultado do processo de extração é armazenado no arquivo:

```text
datasets/processed_data/features.csv
```

### 3. Experimentos no Orange

Instale e abra o **Orange Data Mining**.

Em seguida, abra os arquivos `.ows` disponíveis em:

```text
orange/
```

Esses arquivos contêm os workflows utilizados nos experimentos de aprendizado supervisionado e não supervisionado.

---

## 🔬 Reprodutibilidade

Os principais componentes necessários para reproduzir as análises estão organizados neste repositório:

- dados processados utilizados nos experimentos;
- nomes completos das características extraídas;
- scripts de processamento e extração de características;
- workflows do Orange Data Mining;
- parâmetros utilizados nas principais etapas de análise.

As características automaticamente extraídas seguem as implementações da biblioteca TSFEL.

Os resultados de predição demográfica apresentados na versão revisada do trabalho utilizam validação independente por participante. A identificação biométrica por `ID` utiliza validação cruzada estratificada em cenário *closed-set*.

Devido ao caráter exploratório do estudo e ao número limitado de participantes, os resultados devem ser interpretados dentro das características específicas deste conjunto de dados.

---

## 📚 Trabalho Associado

Este repositório está associado ao trabalho:

> **Mineração de Padrões Biométricos e Demográficos em Sinais de ECG: Um Estudo com Algoritmos de Clusterização e Classificação**

Desenvolvido no Programa de Pós-Graduação em Engenharia Elétrica e Informática Industrial (CPGEI) da Universidade Tecnológica Federal do Paraná (UTFPR).

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

A utilização dos dados deve também respeitar as condições éticas e acadêmicas aplicáveis ao estudo.

---

## 📧 Contato

**Cristian Veggian Matias**

E-mail: [cristianveggian@gmail.com](mailto:cristianveggian@gmail.com)

Lattes: [http://lattes.cnpq.br/4453425163468096](http://lattes.cnpq.br/4453425163468096)

ORCID: [https://orcid.org/0009-0008-1281-3099](https://orcid.org/0009-0008-1281-3099)
