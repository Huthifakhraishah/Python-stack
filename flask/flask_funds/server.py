from flask import Flask, render_template
app = Flask(__name__)   
@app.route('/')         
def hello_world():
    return 'Hello World!'
@app.route('/dojo')         
def hello_dojo():
    return 'Dojo!'
@app.route('/say/<name>')         
def hello_world_name(name):
    return f'Hi {name}!' 
@app.route('/repeat/<number>/<name>')         
def hello(number,name):
    print(name)
    print(number)
    return f"{name}, "*int(number)
if __name__=="__main__":  
    app.run(debug=True)    
