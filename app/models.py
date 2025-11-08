import mysql.connector
from mysql.connector import Error
import os

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "sistema_tarefas"),
            port=int(os.getenv("DB_PORT", "3306")),
            connection_timeout=5,
        )
        return connection
    except Error as e:
        print("Erro ao conectar: " + str(e))
        return None

class Task:
    @staticmethod
    def find_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM tarefas ORDER BY created_at DESC')
        tasks = cursor.fetchall()
        cursor.close()
        conn.close()
        return tasks

    @staticmethod
    def create(data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO tarefas (titulo, descricao) VALUES (%s, %s)',
            (data['titulo'], data['descricao'])
        )
        conn.commit()
        task_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return task_id
