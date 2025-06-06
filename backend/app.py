from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Update with your RDS credentials
conn = mysql.connector.connect(
    host="<RDS-ENDPOINT>",
    user="admin",
    password="<YOUR-PASSWORD>",
    database="taskdb"
)
cursor = conn.cursor(dictionary=True)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (data['title'],))
    conn.commit()
    return jsonify({"message": "Task added."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)