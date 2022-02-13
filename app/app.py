from flask import Flask,redirect,url_for,request,render_template
from Scoring import predict
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/success/<int:storage_id>')
def success(storage_id):
    return "Hello from %d"%storage_id

@app.route('/result', methods =["GET", "POST"])
def index():
    if request.method == "POST":
       # getting input with name = storage_id in HTML form
       storage_id = request.form.get("storage_id")
       return render_template(url_for('success',storage_id = storage_id))
    else:
        return "Not Post Request"

if __name__ == '__main__':
    app.run(debug = True)