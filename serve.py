from flask import Flask
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=['POST'])
def post_protocol():
    subprocess.Popen(["python3", "stress_cpu.py"]) 
    return str("gg")

@app.route("/", methods=['GET'])
def get_protocol():
    return socket.gethostbyname(socket.gethostname())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)