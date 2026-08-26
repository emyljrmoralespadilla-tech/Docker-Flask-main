from flask import Flask, render_template
import mysql.connector

sample = Flask(__name__)

@sample.route('/')
def main():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="sena123",  # nosec B106
            database="082_db",
            connect_timeout=3
        )
        conn.close()
        db_status = "Conexion exitosa a la BD!"
    except Exception as e:
        db_status = f"Error en la conexion: {e}"

    return render_template('index.html', status=db_status)

if __name__ == '__main__':
    sample.run(host="0.0.0.0", port=5050, debug=False)  # nosec B104 B201