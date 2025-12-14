# 🏎️ F1 Race Prediction - 2023 Season Analysis

> Um projeto de Ciência de Dados End-to-End para prever resultados de corridas de Fórmula 1 utilizando Machine Learning.

![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Lib](https://img.shields.io/badge/Library-Scikit--Learn-orange)

## 📋 Sobre o Projeto

Este projeto tem como objetivo prever a **posição final** de um piloto de Fórmula 1 com base em dados prévios à largada (Posição no Grid, Equipe, Piloto e Momento da Temporada).

Utilizando dados reais da temporada 2023 extraídos da **Ergast API (via Jolpica)**, o projeto percorre todo o ciclo de vida de Data Science: desde a engenharia de dados (ETL) até o treinamento de um modelo **Random Forest Regressor**.

## 🧠 Principais Insights & Resultados

O modelo atingiu um **Erro Médio Absoluto (MAE) de 3.32**, o que significa que ele erra a posição final do piloto por cerca de 3 posições.

### O Fator Carro vs. Piloto
Uma das descobertas mais interessantes do modelo foi quantificar a diferença de equipamento. Ao simular cenários hipotéticos, a IA aprendeu que:

* **Max Verstappen (Red Bull)** largando na Pole Position (P1) → Previsão de chegada: **1º Lugar**.
* **Logan Sargeant (Williams)** largando na Pole Position (P1) → Previsão de chegada: **6º Lugar**.

Isso demonstra que o modelo capturou a "falta de ritmo de corrida" da Williams em 2023, mesmo em condições ideais de largada.

### Correlações
* **Grid de Largada:** Tem correlação de **0.56** com a posição final. É o fator mais decisivo, mas não único.
* **Evolução das Equipes:** A feature `Round` (número da corrida) apareceu como 2ª mais importante, indicando que o modelo percebeu a mudança de força das equipes (como a melhora da McLaren) ao longo do ano.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas:** Manipulação e limpeza de dados (Data Wrangling).
* **Requests:** Consumo de API REST com paginação automatizada.
* **Seaborn/Matplotlib:** Visualização de dados (Heatmaps, Scatter Plots).
* **Scikit-Learn:**
    * `RandomForestRegressor` (Modelagem).
    * `train_test_split`, `mean_absolute_error` (Validação).
    * `OneHotEncoder` (via pandas get_dummies).

## 📂 Estrutura do Projeto

```text
f1-prediction/
│
├── data/
│   ├── raw/               # Dados brutos baixados da API (CSV)
│   └── processed/         # Dados limpos e prontos para o modelo
│
├── notebooks/
│   ├── 01_coleta_dados.ipynb       # Script de ingestão da API
│   ├── 02_limpeza.ipynb            # Conversão de tempos e tratamento de nulos
│   ├── 03_eda.ipynb                # Análise Exploratória e Gráficos
│   ├── 04_feature_engineering.ipynb # One-Hot Encoding
│   └── 05_modelagem.ipynb          # Treinamento e Avaliação do ML
│
├── src/                   # Scripts auxiliares (.py)
├── README.md              # Documentação do projeto
└── requirements.txt       # Dependências do projeto