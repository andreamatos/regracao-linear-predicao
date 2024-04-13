# Previsão de Preços de Imóveis em São Paulo

Este é um programa Python que utiliza um modelo de regressão linear para prever os preços de imóveis na cidade de São Paulo com base em diversas características, como área, número de quartos, banheiros, etc.

## Passos do Programa

### 1. Carregar os Dados

Os dados dos imóveis são carregados de um arquivo CSV chamado 'sao-paulo-properties-april-2019.csv' usando a biblioteca pandas.

### 2. Separar Features e Target

As variáveis independentes (features) são separadas da variável dependente (target), que é o preço do imóvel.

### 3. Separar Dados Numéricos e Categóricos

As features são divididas em duas partes: numéricas e categóricas, utilizando o método `select_dtypes` do pandas.

### 4. Dividir os Dados em Conjuntos de Treinamento e Teste

Os dados são divididos em conjuntos de treinamento e teste usando a função `train_test_split` do scikit-learn.

### 5. Pré-processamento dos Dados

Pipeline é configurado para pré-processar os dados numéricos e categóricos separadamente. Isso inclui preenchimento de valores faltantes com a média para dados numéricos e com o valor mais frequente para dados categóricos, bem como codificação one-hot para variáveis categóricas.

### 6. Criar e Treinar o Modelo de Regressão Linear

Um modelo de regressão linear é configurado utilizando o pré-processador criado e o regressor de regressão linear do scikit-learn. O modelo é treinado utilizando os dados de treinamento.

### 7. Fazer Previsões

Um conjunto de dados de teste é criado manualmente (apenas um exemplo de entrada) e utilizado para fazer previsões utilizando o modelo treinado.

### 8. Formatar a Saída

O preço previsto é convertido de centavos de real para reais e formatado como moeda brasileira.

### 9. Imprimir o Preço Previsto

O preço previsto é impresso na tela.

## Requisitos

Antes de executar o programa, certifique-se de ter as seguintes bibliotecas Python instaladas:

- pandas
- numpy
- scikit-learn

Você pode instalar essas bibliotecas usando pip:

pip install pandas numpy scikit-learn


## Como Usar

1. Clone este repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git


2. Navegue até o diretório do projeto:

cd seu-repositorio


3. Execute o script Python:

python predicao.py


Isso carregará os dados de imóveis de um arquivo CSV, treinará um modelo de regressão linear e fará uma previsão de preço para um exemplo de imóvel.

## Arquivos

- `predicao.py`: O script principal que contém o código para carregar dados, treinar o modelo e fazer previsões.
- `sao-paulo-properties-april-2019.csv`: O conjunto de dados usado para treinar o modelo.
- `Readme.md`: Este arquivo que fornece informações sobre o projeto.

## Contribuição

Contribuições são bem-vindas! Se você quiser melhorar este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.
