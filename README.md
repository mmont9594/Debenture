# ETL - Debênture e XML de Fundos de Investimento

[![Linkedin](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white&style=for-the-badge)](https://www.linkedin.com/in/matheus-monteiro)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge)
![R](https://img.shields.io/badge/R-276DC3?logo=r&logoColor=white&style=for-the-badge)

## Overview

Objetivo é criar funções para processar e automatizar os arquivos que se encontram na pasta **~/Files/**:
- Registros Consolidados **.csv**
- Informações de Companhias Abertas **.csv**
- XML de Fundos **.XML**
- Titulos Privados Características **.xls**

Essa é uma estrutura inicial, onde a partir do que foi feito é possível tratar cada um dos arquivos separadamente e exportar para Excel contendo uma estrutura estruturada, formatada e pronta para ser importada num BI para análises e visualizações

O código foi feito em duas linguagens, Registros, Informações de companhias e características dos Fundos foi desenvolvido em **Python** a parte do XML de fundos foi feita em **R**.

## Instruções

- [Instalação](#instalacao)
- [Utilização](#utilizacao)
- [Contato](#contribuicao)


# Instalação

Para começar o projeto, siga os seguintes passos:

1. Clone o repositório na sua máquina local:

   ```bash
   git clone https://github.com/mmont9594/Debenture.git

2. Navegue até o diretório:

   ```bash
   cd Debenture

3. Instale as bibliotecas necessárias para execução:

   ```bash
   pip install -r requirements.txt

# Utilização

## Utilizando o Projeto

### Python Script

O projeto foi feito de forma simples, refatorado para uma melhor execução e compreensão. Podendo no futuro ser aperfeiçoado para uma maior abstração e integração com outros serviços.

#### 1. PrivateInfo.py
Descrição: O arquivo PrivateInfo.py processa o arquivo titulos privados características **.xls**, ele estrutura todo ETL, formatando e criando novas variáveis que serão utilizadas para monitorando e avaliação diárias dos títulos. Foi feito para atender a demanda de uma atualização diária para processamento das novas informações

#### 2. Registros.py
Descrição: O arquivo Registros.py processa os arquivos registros consolidados **.csv**, segue a mesma lógica do PrivateInfo.py levando em consideração seu layout e como podemos utilizar essas informações diariamente

#### 3. main.py
Descrição: O arquivo main.py como executar do projeto. ele é vinculado com todas as outras funções para execução do ETL de cada um dos arquivos.

#### 4. CadCiaAbertas.py
Descrição: O arquivo CadCiaAbertas.py carrega as informações contidas no arquivo, e exporta para um data.frame

### Exemplo:

Exemplo de como executar o scrit python para gerar o arquivo com as informações tratadas das Debêntures:

  ```python
  # Import the Libraries
  import pandas as pd
  from CadCiaAbertas import carregar_info_cia_abertas
  from Registros import carregar_tratar_info_registros_consolidados
  from PrivateInfo import carregar_tratar_info_titulos_privados

  # Execute o scrit definindo os parâmetros necessários
  carregar_info_ativos_exportar(Gerar_Excel=True, exportar=False, Ativo='DEB', Titulo='Debênture')
```

### R Script

#### 1. xmlFundosETL.R
Descrição: O arquivo xmlFundosETL.R é responsável por processar as informações contidas nos arquivos **.XLM**, e exporta para um Excel consolidando toda estrutura contida neles. Como sugestão, também pontuada no código, seria melhor para análise e estrutura de dados segmentarmos dentro de um mesmo output **sheets** contendo cada ativo para não carregarmos sujeira dentro de uma grande tabela final.

  ```R
# Caso seja sua primeira interação com R, recomendo seguir o passo a passo para executar corretamente.
# Caso já tenha instalado em seu ambiente os pacotes abaixo, defina como FALSE o parâmetro instalar_pacotes
# dplyr, xml2, writexl, magrittr, dplyr
prep_ambiente(instalar_pactoes=FALSE) 

# Após isso, execute o código xmlFundosETL definindo o path de onde os arquivos se encontram e seu formato
xmlFundosETL(path = '/Debenture/Files/', formato = '.XML')
```

## Contato

### Qualquer dúvida, pode entrar em contato comigo:

**Matheus Monteiro**
- LinkedIn: [Matheus Monteiro](https://www.linkedin.com/in/matheus-monteiro/)
