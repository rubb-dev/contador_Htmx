from flask import Flask, render_template

app = Flask(__name__)

# Inicializamos el contador en 0
contador = 0

@app.route('/')
def index():
    return render_template('index.html', contador=contador)

@app.route('/incrementar')
def incrementar():
    global contador
    contador += 1
    return str(f'<span id="contador">{contador}</span>')

@app.route('/decrementar')
def decrementar():
    global contador
    contador -= 1
    return str(f'<span id="contador">{contador}</span>')

if __name__ == '__main__':
    app.run(debug=True)
