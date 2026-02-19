#  Student Exam Performance Indicator

##  Sobre o Projeto

Este é um projeto de **Machine Learning End-to-End** desenvolvido para analisar como o desempenho acadêmico (notas em testes) é impactado por variáveis pessoais e socioeconômicas.

O objetivo principal é construir um modelo preditivo capaz de estimar a nota de **Matemática** de um aluno com base em características como Gênero, Etnia, Escolaridade dos Pais, Tipo de Almoço e curso preparatório. O projeto abrange desde a ingestão de dados até o deploy de uma aplicação web interativa.

---

##  Tecnologias Utilizadas

| Categoria | Ferramentas |
| --- | --- |
| **Linguagem** | Python 3.8+ |
| **Manipulação de Dados** | Pandas, NumPy |
| **Visualização** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn, XGBoost, CatBoost, AdaBoost |
| **Web Framework** | Flask |
| **Frontend** | HTML/CSS (Bootstrap) |

---

##  Estrutura do Projeto

A arquitetura segue um padrão modular para garantir escalabilidade e facilitar a manutenção:

```text
├── artifacts/               # Modelos treinados e processadores (PKL)
├── src/                     # Código fonte do projeto
│   ├── components/
│   │   ├── data_ingestion.py    # Ingestão e divisão treino/teste
│   │   ├── data_transformation.py # Pré-processamento e Feature Engineering
│   │   └── model_trainer.py     # Treinamento e avaliação de modelos
│   ├── pipeline/
│   │   └── predict_pipeline.py  # Pipeline de inferência para novos dados
│   ├── logger.py            # Logs da aplicação
│   └── exception.py         # Tratamento de exceções customizadas
├── templates/               # Páginas HTML (Flask)
├── app.py                   # Ponto de entrada da aplicação Flask
└── requirements.txt         # Dependências do projeto

```

---

##  Como Executar

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

```

### 2. Criar e Ativar Ambiente Virtual

```bash
conda create -p venv python=3.8 -y
conda activate venv/

```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt

```

### 4. Executar a Aplicação

```bash
python app.py

```

Acesse no seu navegador: `http://127.0.0.1:5000`

---

##  Resultados dos Modelos

Durante a fase de experimentação, diversos algoritmos de regressão foram testados. O modelo final foi selecionado com base na métrica **R2 Score**.

> [!TIP]
> Os artefatos gerados (`model.pkl` e `preprocessor.pkl`) são salvos automaticamente na pasta `artifacts/` após o treinamento, permitindo que a aplicação realize predições em tempo real sem necessidade de re-treinar o modelo.

---



