from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    with open("counter.txt", "r+") as file:
        count = int(file.read()) + 1
        file.seek(0)
        file.write(str(count))
    return render_template('index.html', visits=count)

if __name__ == '__main__':
    # Inicializa el contador solo si el archivo está vacío
    with open("counter.txt", "a+") as f:
        f.seek(0)
        if not f.read():
            f.write("0")
    # Ejecuta el servidor Flask solo en modo desarrollo
    app.run(debug=True)
