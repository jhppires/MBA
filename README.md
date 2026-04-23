# MBA em Engenharia de Dados / Data Science - Python Exercises & Study Repository

# 📚 Python Exercises & Study Repository

Repositório dedicado a exercícios, experimentos e estudos realizados durante minha pós-graduação e evolução em Engenharia de Dados / Data Science.

---

## 🧠 Objetivo

Centralizar:

* exercícios práticos
* testes de conceitos
* pequenos projetos
* estudos de ferramentas e bibliotecas

Foco em aprendizado contínuo e organização do conhecimento.

---

## ⚙️ Setup do Ambiente

Este projeto utiliza um setup profissional para garantir reprodutibilidade e isolamento.

### 🐍 Python Version Manager

Utilizo **pyenv** para gerenciar versões do Python.

### 📦 Gerenciamento de Dependências

Utilizo **Poetry** para:

* criação de ambientes virtuais
* gerenciamento de dependências

### 🧰 Ferramentas Globais

Utilizo **pipx** para instalar ferramentas isoladas (como Poetry, linters, etc).

---

## 🏗️ Estrutura do Projeto

```bash
.
├── exercises/        # exercícios isolados
├── notebooks/       # estudos exploratórios
├── scripts/         # scripts utilitários
├── data/            # dados de teste (se houver)
├── pyproject.toml   # config do Poetry
└── README.md
```

---

## 🚀 Como rodar o projeto

### 1. Clonar repositório

```bash
git clone <repo>
cd <repo>
```

### 2. Instalar dependências

```bash
poetry install --no-root
```

### 3. Ativar ambiente

```bash
poetry shell
```

ou rodar diretamente:

```bash
poetry run python script.py
```

---

## 📌 Configuração recomendada

Garantir que o Poetry cria ambientes dentro do projeto:

```bash
poetry config virtualenvs.in-project true
```

---

## 🧪 Padrão de uso

* Cada experimento deve ser isolado
* Evitar dependências desnecessárias
* Priorizar clareza e organização
* Código voltado para aprendizado, não produção

---

## 📈 Evolução esperada

Este repositório pode evoluir para:

* pipelines de dados
* projetos de ETL
* testes com APIs
* integrações com bancos de dados
* estudos de machine learning

---

## 🧠 Observação

Este não é um repositório de produção — é um ambiente de aprendizado estruturado.
