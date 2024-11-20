from flask import Flask, render_template,make_response

app = Flask(__name__)

@app.route("/")
def portada():
    return render_template("portada.html")

@app.route('/mostrarmapa')
def mostrarmapa():


    return render_template('mapapredic.html')
    


@app.route('/informacion')
def informacion():

    return render_template('informacion.html')

@app.route('/satelite')
def satelite():

    return render_template('satelite.html')

if __name__ == '__main__':
    app.run(debug=True, port=5010)
    