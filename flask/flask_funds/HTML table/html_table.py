from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def checkboard():
    users = [
    {'fname' : 'Michael', 'lname' : 'Choi'},
    {'fname' : 'John', 'lname' : 'Supsupin'},
    {'fname' : 'Mark', 'lname' : 'Guillen'},
    {'fname' : 'KB', 'lname' : 'Tonel'}
    ]
    return render_template('html_table.html',users=users)
if __name__ == "__main__":
    app.run(debug=True)