from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload_replay", methods=["POST"])
def upload_replay():
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save("uploads/" + f.filename)
        return render_template("upload_acknowledge.html", replay_name = f.filename)