from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    with open("counter.txt", "r+") as file:
        count = int(file.read()) + 1
        file.seek(0)
        file.write(str(count))
    return render_template('index.html', visits=count)

if __name__ == '__main__':
    # Inicializa counter.txt si está vacío
    with open("counter.txt", "a+") as f:
        f.seek(0)
        if not f.read():
            f.write("0")
    # Usa el puerto asignado por Digital Ocean o 5000 para desarrollo local
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
