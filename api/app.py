from flask import Flask,render_template,request
app = Flask(__name__,static_url_path='/SSE-LAB2_static', static_folder='./static')

@app.route("/")
def hello_world():
    return render_template("index.html")
    # return "Hello , my new app!"

@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)