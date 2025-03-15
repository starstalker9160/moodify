from threading import Timer
from backend.helper import *
from backend.exceptions import *
from webbrowser import open as webbrowser_open
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    send_from_directory,
    url_for,
    redirect,
)

print("[  OK  ] Starting app...")

k = "[" + foreplay() + "]"
if k not in ["[I-11]", "[I-22]"]:
    raise InitializationErr(f"App unable to initialize, failed with error code: {k}")
else:
    print(f"[  OK  ] App initialized successfully; code: {k}")


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fill-out")
def fill_out():
    return render_template("sliders.html")

@app.route("/journal")
def journal():
    return render_template("journal.html")


@app.errorhandler(404)
def not_found_404(e):
    return render_template("404.html"), 404


@app.errorhandler(405)
def not_found_405(e):
    return render_template("405.html"), 405


if __name__ == "__main__":
    try:
        app.run(host="127.0.0.1", port=8080, debug=False)
        # Timer(1, lambda: webbrowser_open("http://127.0.0.1:8080")).start()
    except Exception as e:
        print(f"[ FAIL ] Error: {e}")