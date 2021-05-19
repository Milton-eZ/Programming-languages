from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/mejores_juegos')
def playlist():
    topJuegos=("Call of Duty: Warzone","Minecraft","Fornite",
                "Among Us","League of Legends","Apex Legends","CS'  GO")
    return render_template('mejores_juegos.html', juegos=topJuegos)

@app.route('/generos')
def generos():
    return render_template('generos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html') 

if __name__ == '__main__':
    app.run(debug=True)