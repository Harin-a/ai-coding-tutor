import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        dbname="ai_tutor",
        user="postgres",
        password="anilkumar2468@",  # Replace with your PostgreSQL password
        host="localhost",
        port="5432"
    )
    return conn

@app.route('/')
def hello():
    return 'AI Coding Tutor API'

@app.route('/test_db')
def test_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({'db_version': db_version[0]})

if __name__ == '__main__':
    app.run(debug=True)