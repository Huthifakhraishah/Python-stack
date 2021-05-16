from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def first():
    return render_template("server.html")
@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    name = request.form['name']
    location = request.form['location']
    favourite = request.form['favourite']
    comment = request.form['comment']
    radio = request.form['radio']
    check = request.form['check']
    return render_template("result.html", name=name,favourite=favourite,comment=comment,location=location,check=check,radio=radio)
if __name__ == "__main__":
    app.run(debug=True)
