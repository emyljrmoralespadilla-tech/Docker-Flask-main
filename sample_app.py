import os
from flask import Flask, render_template
import pymysql

sample = Flask(__name__)

@sample.route("/")
def home():
    try:
        conn = pymysql.connect(
            host=os.getenv("DB_HOST", "servidor-bd-ejemplo"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME", "082_db"),
            connect_timeout=3
        )
        conn.close()
        db_status = "Conexion exitosa a la BD!"
    except Exception as e:
        db_status = f"Error en la conexion: {e}"

    return render_template("index.html", db_status=db_status)

if __name__ == '__main__':
    sample.run(port=5050, debug=False)