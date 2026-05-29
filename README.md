# GeekStore

API de e-commerce geek desenvolvida com FastAPI para gerenciamento de produtos e processamento de compras.

## 📋 Sobre o projeto

O GeekStore é uma aplicação backend construída em Python utilizando FastAPI. O sistema disponibiliza endpoints para:

* Listagem de produtos
* Processamento de compras
* Aplicação de descontos
* Simulação de gateway de pagamento

Além da API, o projeto inclui:

* Testes unitários
* Testes BDD com pytest-bdd
* Testes de API com Tavern
* Testes E2E com Selenium

---

## 🛠️ Tecnologias utilizadas

* Python 3
* FastAPI
* Uvicorn
* Pytest
* Selenium
* Tavern
* Pytest-BDD

---

## 📁 Estrutura do projeto

```text
GeekStore/
├── app/
│   ├── core/
│   │   └── database.py
│   ├── models/
│   │   ├── product.py
│   │   └── purchase.py
│   ├── repositories/
│   │   └── product_repository.py
│   ├── routes/
│   │   ├── order_routes.py
│   │   └── product_routes.py
│   ├── services/
│   │   ├── discount_service.py
│   │   ├── order_service.py
│   │   └── payment_service.py
│   ├── static/
│   │   └── index.html
│   └── main.py
│
├── tests/
│   ├── features/
│   ├── selenium/
│   ├── tavern/
│   ├── test_order_service.py
│   └── test_products.py
│
├── requirements.txt
└── README.md
```

---

## ▶️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd GeekStore
```

### 2. Crie um ambiente virtual

#### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8000
```

Documentação automática da API:

```text
http://127.0.0.1:8000/docs
```

---

## 📦 Endpoints da API

### Listar produtos

```http
GET /api/produtos
```

### Realizar compra

```http
POST /api/comprar
```

### Exemplo de payload

```json
{
  "product_id": 1,
  "quantity": 2,
  "payment_method": "cartao"
}
```

---

## 🧪 Executando os testes

### Testes unitários

```bash
pytest
```

### Testes com cobertura

```bash
pytest --cov=app
```

### Testes BDD

```bash
pytest tests/features
```

### Testes de API com Tavern

```bash
pytest tests/tavern
```

### Testes E2E com Selenium

```bash
pytest tests/selenium
```

---

## ⚙️ Funcionalidades implementadas

* Cadastro inicial de produtos
* Consulta de catálogo
* Processamento de pedidos
* Aplicação de descontos
* Integração simulada de pagamento
* Interface HTML simples
* Cobertura de testes automatizados

---

## 📚 Arquitetura utilizada

O projeto segue uma arquitetura em camadas:

* **Routes** → definição dos endpoints
* **Services** → regras de negócio
* **Repositories** → acesso aos dados
* **Models** → modelos e validações
* **Core** → configuração e infraestrutura

Essa separação facilita:

* manutenção
* testes
* reutilização de código
* escalabilidade

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos.
