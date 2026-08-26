import os
from flask import Flask

sample = Flask(__name__)

# Solución Bandit: Clave mediante variable de entorno
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')

@sample.route('/')
def main():
    # Solución Pytest: Código HTTP 200 OK
    return "OK", 200

if __name__ == "__main__":
    # Solución Bandit: Desactivar modo debug
    sample.run(host="0.0.0.0", port=5050, debug=False)