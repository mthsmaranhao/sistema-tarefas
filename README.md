# 🗂️ Sistema de Gerenciamento de Tarefas (Flask + MySQL)

Aplicação **backend** desenvolvida em **Python (Flask)** com banco de dados **MySQL**, responsável por gerenciar uma lista de tarefas com endpoints RESTful.  
O projeto foi estruturado seguindo boas práticas de organização de código, separando as responsabilidades em rotas, modelos e inicialização da aplicação.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **Flask 3.0**
- **Flask-CORS 4.0**
- **MySQL Connector 8.2**
- **python-dotenv 1.0**

---

## 🏗️ Estrutura do Projeto

```bash
backend-python/
├── app/
│   ├── __init__.py         # Inicializa o Flask e registra os blueprints
│   ├── models.py           # Conexão e operações no banco de dados MySQL
│   └── routes.py           # Rotas HTTP da API
│
├── run.py                  # Ponto de entrada da aplicação
├── requirements.txt        # Dependências do projeto
└── .env                    # Variáveis de ambiente

⚙️ Configuração do Ambiente
1️⃣ Clone o repositório
git clone https://github.com/mthsmaranhao/sistema-tarefas.git
cd sistema-tarefas/backend-python

2️⃣ Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Configure o arquivo .env

Crie (ou edite) o arquivo .env na raiz do backend:

DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=root123
DB_NAME=sistema_tarefas
DB_PORT=3306


💡 Use o mesmo usuário e senha configurados no seu MySQL Workbench.

🧱 Banco de Dados

Execute no MySQL (Workbench ou terminal):

CREATE DATABASE IF NOT EXISTS sistema_tarefas;
USE sistema_tarefas;

CREATE TABLE IF NOT EXISTS tarefas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(255) NOT NULL,
  descricao TEXT,
  concluida BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO tarefas (titulo, descricao, concluida) VALUES
('Estudar Flask', 'Criar API simples', FALSE),
('Revisar SQL', 'JOINs e subconsultas', TRUE);

▶️ Execução

Rode o servidor:

python run.py


Se tudo estiver certo, você verá:

 * Running on http://127.0.0.1:3000

🌐 Endpoints da API
Método	Rota	Descrição
GET	/api/	Verifica o status da API
GET	/api/tasks	Lista todas as tarefas
POST	/api/tasks	Cria uma nova tarefa (em breve)
PUT	/api/tasks/<id>	Atualiza uma tarefa (em breve)
DELETE	/api/tasks/<id>	Remove uma tarefa (em breve)


🧩 Exemplo de Resposta (GET /api/tasks)
[
  {
    "id": 1,
    "titulo": "Estudar Flask",
    "descricao": "Criar API simples",
    "concluida": 0,
    "created_at": "2025-11-08T00:00:00",
    "updated_at": "2025-11-08T00:00:00"
  },
  {
    "id": 2,
    "titulo": "Revisar SQL",
    "descricao": "JOINs e subconsultas",
    "concluida": 1,
    "created_at": "2025-11-08T00:00:00",
    "updated_at": "2025-11-08T00:00:00"
  }
]

💡 Melhorias Futuras

 Adicionar endpoints POST, PUT e DELETE

 Implementar autenticação de usuários

 Adicionar frontend em Vue.js

 Criar testes automatizados (pytest)

 Implementar logs e tratamento de erros

👨‍💻 Autor

Matheus Maranhão 
