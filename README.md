# 🗂️ Sistema de Gerenciamento de Tarefas (Flask + MySQL)

Aplicação **backend** desenvolvida em **Python (Flask)** com banco de dados **MySQL**, responsável por gerenciar uma lista de tarefas com endpoints RESTful.  
O projeto foi estruturado seguindo boas práticas de organização de código, separando as responsabilidades em rotas, modelos e inicialização da aplicação.

---

## ⚙️ Configuração do Ambiente

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/mthsmaranhao/sistema-tarefas.git
cd sistema-tarefas/backend-python
```

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

Execute os comandos abaixo no MySQL (Workbench ou terminal):
```
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
```

▶️ Execução

Rode o servidor com o comando:

python run.py


Se tudo estiver certo, o terminal exibirá:

 * Running on http://127.0.0.1:3000


Acesse no navegador:

http://127.0.0.1:3000/api/tasks

🌐 Endpoints da API
Método	Rota	Descrição
GET	/api/	Verifica o status da API
GET	/api/tasks	Lista todas as tarefas
POST	/api/tasks	Cria uma nova tarefa (em breve)
PUT	/api/tasks/<id>	Atualiza uma tarefa (em breve)
DELETE	/api/tasks/<id>	Remove uma tarefa (em breve)

## 🧩 Exemplo de Requisição e Resposta

### 📥 Endpoint
`GET /api/tasks`

Retorna todas as tarefas cadastradas no banco de dados.

### 🧠 Exemplo de Requisição

```bash
curl -X GET http://127.0.0.1:3000/api/tasks
📤 Exemplo de Resposta (200 OK)
json
Copiar código
[
  {
    "id": 1,
    "titulo": "Estudar Flask",
    "descricao": "Criar API simples utilizando o framework Flask",
    "concluida": false,
    "created_at": "2025-11-08T10:32:00",
    "updated_at": "2025-11-08T10:32:00"
  },
  {
    "id": 2,
    "titulo": "Revisar SQL",
    "descricao": "Estudar comandos JOIN, GROUP BY e subconsultas",
    "concluida": true,
    "created_at": "2025-11-08T11:10:00",
    "updated_at": "2025-11-08T11:12:00"
  }
]
```

💡 Melhorias Futuras
```
 Adicionar endpoints POST, PUT e DELETE

 Implementar autenticação de usuários

 Adicionar frontend em Vue.js

 Criar testes automatizados (pytest)

 Implementar logs e tratamento de erros

🧠 Estrutura do Projeto
backend-python/
├── app/
│   ├── __init__.py         # Inicializa o Flask e registra os blueprints
│   ├── models.py           # Conexão e operações no banco de dados MySQL
│   └── routes.py           # Rotas HTTP da API
│
├── run.py                  # Ponto de entrada da aplicação
├── requirements.txt        # Dependências do projeto
└── .env                    # Variáveis de ambiente
```
👨‍💻 Autor

Matheus Maranhão
