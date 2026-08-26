from flask import Flask

sample = Flask(__name__)

# Fallo Bandit (B105): Clave en texto plano
MYSQL_PASSWORD = "super_secret_123"

@sample.route('/')
def main():
    # Fallo Pytest: Código de estado 500
    return "Internal Server Error", 500

if __name__ == "__main__":
    # Fallo Bandit (B201): Modo depuración activado
    sample.run(host="0.0.0.0", port=5050, debug=True)