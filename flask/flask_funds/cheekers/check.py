from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def checkboard():
    return render_template('index.html', width=8, height=8,color1="black",color2="green" )
@app.route('/<x>')
def chh(x):
    return render_template('index.html', width=8, height=int(x),color1="black",color2="green" )
@app.route('/<x>/<y>')
def chhd(x, y):
    return render_template('index.html', width=int(x), height=int(y),color1="black",color2="green" )
@app.route('/<x>/<y>/<color1>/<color2>')
def chhds(x, y, color1, color2):
    return render_template('index.html', width=int(x), height=int(y), color1= color1, color2=color2)
if __name__ == "__main__":
    app.run(debug=True)