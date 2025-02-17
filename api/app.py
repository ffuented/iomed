from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_api():
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="myuser",
        password="mypassword",
        host="db"
    )
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({'db_version': db_version})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
