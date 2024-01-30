from flask import Flask
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=['POST'])
def post_protocol():
    subprocess.Popen(["python3", "stress_cpu.py"]) 


@app.route("/", methods=['GET'])
def get_protocol():
    return socket.gethostbyname(socket.gethostname())

if __name__ == '__main__':
    processes = cpu_count()
    pool = Pool(processes)
    print(pool.map(stress_cpu, [11000000, 110000000]))
    print("time cost : ", time.time() - start_time)
    #app.run(host='0.0.0.0', port=5000)
    #app.run(host='0.0.0.0', port=5000)
