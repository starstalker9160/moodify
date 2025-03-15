from backend.helper import *
from backend.exceptions import *
from flask import Flask, render_template

k = "[" + foreplay() + "]"
if k not in ["I-11", "I-22"]:
    raise InitializationErr(f"App unable to initialize, failed with error code: {k}")
else:
    print(f"App initialized successfully; code: {k}")


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
