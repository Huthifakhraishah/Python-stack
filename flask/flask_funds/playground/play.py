from flask import Flask, render_template
app = Flask(__name__) 
@app.route('/play')         
def index():
    return render_template("play.html",num=3,backgorund_color="blue")
@app.route('/play/<snum>')
def main(snum):
    return render_template("play.html", num = int(snum),backgorund_color="blue")
@app.route('/play/<snum>/<color>')
def main_one(snum,color):
    return render_template("play.html", num = int(snum), backgorund_color=color)
if __name__=="__main__":  
    app.run(debug=True)     
