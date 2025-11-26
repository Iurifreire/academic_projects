# 📄 PROJETO A3 -- MATRIZES: Cálculo pelo Método de Cramer

## 👨‍👩‍👧‍👦 Integrantes do Grupo

- Iuri Freire E. de Almeida – *RA: 12724141707*
- Fillype da Silva Araujo - *RA: 12724145904*
- Vinicius de Jesus Rocha Reis - *RA: 12724120214*
- Duilio do Nascimento Brandão - *RA: 12724216242*
- Diego de Lima Gomes - *RA: 12724124220*
- Vinicius dos Santos Santana - *RA: 12724121934*
------------------------------------------------------------------------
## Relatório

O relatorio pode ser acessado pelo link abaixo:

https://docs.google.com/document/d/1ouCZQFW4T4jl7nGwVftfg8__dKE4enlo/edit?usp=drivesdk&ouid=102608216915985358617&rtpof=true&sd=true
---
## 🧾 Descrição do Projeto

O **PROJETO A3 -- MATRIZES: Calcular Cramer** é uma aplicação dividida
em **frontend** e **backend**, funcionando como um sistema integrado
para resolução de sistemas lineares usando o **Método de Cramer**.

### ✅ Funcionalidades Principais

-   Entrada de matriz e vetor de resultados\
-   Cálculo do determinante principal\
-   Geração dos determinantes auxiliares\
-   Cálculo das incógnitas pelo método de Cramer\
-   Exibição visual dos passos\
-   Tratamento de erros quando o sistema não possui solução única

### 🛠 Tecnologias Utilizadas

-   **Frontend:** React.js\
-   **Backend:** Python + Flask\
-   **API REST:** Comunicação entre as camadas\
-   **Matemática:** Implementação própria de cálculo de determinantes

------------------------------------------------------------------------

## ⚙️ Pré-requisitos

### Geral

Antes de iniciar, certifique-se que possui:

-   **Git**
-   **Python 3.10+**
-   **Node.js 18+**
-   **NPM ou Yarn**

### Backend

-   Python + Flask\
-   Ambiente virtual recomendado

### Frontend

-   Node.js + npm/yarn

------------------------------------------------------------------------

## 📦 Instalação de Dependências

### 1. Baixar o projeto

Após extrair, você terá:
    .gitignore
    README.md
    frontend/
    backend/

### 2. Backend

Entre na pasta:

``` bash
cd backend
```

Crie o ambiente virtual:

``` bash
python -m venv venv
```

Ative o ambiente:

-   **Windows**

    ``` bash
    venv\Scripts\activate
    ```

-   **Linux/Mac**

    ``` bash
    source venv/bin/activate
    ```

Instale as dependências:

``` bash
pip install -r requirements.txt
```

Caso o arquivo não exista:

``` bash
pip install flask flask-cors
```

------------------------------------------------------------------------

### 3. Frontend

Entre na pasta:

``` bash
cd frontend
```

Instale as dependências:

``` bash
npm install
```

ou

``` bash
yarn
```

------------------------------------------------------------------------

## ▶️ Execução do Projeto

### ✅ Iniciar o Backend

Dentro da pasta `backend`:

``` bash
python src/index.py
```

O servidor será iniciado em:

    http://localhost:5000

------------------------------------------------------------------------

### ✅ Iniciar o Frontend

Dentro da pasta `frontend`:

``` bash
npm start
```

ou

``` bash
yarn start
```

A aplicação abrirá em:

    http://localhost:3000

O frontend se comunica com o backend por meio do arquivo:

    frontend/src/services/api.js

------------------------------------------------------------------------

## ✅ Conclusão

Este projeto integra frontend e backend para fornecer uma ferramenta
completa de cálculo utilizando o **Método de Cramer**, apresentando os
resultados e etapas de forma intuitiva e interativa.
