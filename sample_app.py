from flask import Flask

sample = Flask(__name__)
MYSQL_PASSWORD = "super_secret_123"  # Bandit: Clave quemada en texto plano (B105)

@sample.route('/')
def main():
    return "Error interno del servidor", 500  # Pytest: Código de estado fallido

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, debug=True)  # Bandit: Modo debug activado (B201)