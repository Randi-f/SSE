from flask import Flask, render_template, request

app = Flask(__name__, static_url_path="/SSE-LAB2_static", static_folder="./static")


@app.route("/")
def hello_world():
    return render_template("index.html")
    # return "Hello , my new app!"


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    if input_age < "18":
        return render_template("hello.html", name=input_name, age=input_age)
    else:
        return render_template("helloAdult.html", name=input_name, age=input_age)


def process_query(query):
    if "largest" in query:
        # Which of the following numbers is the largest: 66, 72, 44?
        query = query.replace("?", "")
        query = query.replace(",", "")
        factors = query.split(" ")
        return str(max(int(factors[8]), int(factors[9]), int(factors[10])))
    if "plus" in query:
        query = query.replace("?", "")
        factors = query.split(" ")
        return str((int)(factors[2]) + (int)(factors[4]))
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    if query == "What is your name?":
        return "Aoligei"
    # What is 27 plus 75?
    # Which of the following numbers is the largest: 7, 78, 82?
    else:
        return "Unknown"


@app.route("/query", methods=["GET"])
def query_handler():
    query_param = request.args.get("q", "")
    result = process_query(query_param)
    msg = (
        """<html><body>""" + result + """
    Let me show you one in 3 seconds!
    <script>
        setTimeout(function(){
        window.location.href = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dkfindout.com%2Fus%2Fdinosaurs-and-prehistoric-life%2Fdinosaurs%2Fwhat-is-dinosaur%2F&psig=AOvVaw0YwZbs91uCBimJC1hiKE3c&ust=1698345280911000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCKipmqvrkYIDFQAAAAAdAAAAABAE';
        }, 3000); // 3000ms（3s）
    </script>
    </body>
    </html>
    """
    )
    if result == "dinasours":
        return msg
    if result == "Aoligei":
        return result
    if result == "Unknown":
        return (
            result + " . Please try this link: https://sse-sf.vercel.app/query?q=dinosaurs"
        )

    return result
