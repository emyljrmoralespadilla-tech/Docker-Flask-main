from flask import Flask

sample = Flask(__name__)

@sample.route('/')
def main():
    return "OK", 200

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, debug=False)  # nosec B104