from threading import Timer
from backend.helper import *
from backend.exceptions import *
from webbrowser import open as webbrowser_open
from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

print("[  OK  ] Starting app...")

k = "[" + initialize() + "]"
if k not in ["[I-11]", "[I-22]"]:
    raise InitializationErr(f"App unable to initialize, failed with error code: {k}")
else:
    print(f"[  OK  ] App initialized successfully; code: {k}")


data_ = None
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

@app.route("/response")
def response():
    k = handle(data_)
    return render_template("response.html", response="Something went wrong in generating a response...\nWe're sorry about that" if k is None else k)


@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = request.get_json()
        print(data)

        if not isinstance(data, dict):
            raise InvalidJSONFormat("Not proper JSON, failed with error code: [P-01]")

        required_keys = ["happy", "anger", "anxiousness"]

        if not all(key in data for key in required_keys):
            raise InvalidJSONFormat("Weird keys in JSON data, failed with error code: [P-02]")

        if not all(1 <= data[key] <= 5 for key in required_keys if isinstance(data[key], int)):
            raise InvalidJSONFormat("Invalid values for JSON keys, failed with error code: [P-03]")

        print("[  OK  ] POST successful, generating response")

        global data_
        data_ = data

        return jsonify(data)

    except InvalidJSONFormat as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        print("Legitimately no idea what the hell happened")
        return jsonify({"error": "Invalid data received"}), 400


@app.errorhandler(404)
def not_found_404(e):
    return render_template("404.html"), 404


@app.errorhandler(405)
def not_found_405(e):
    return render_template("405.html"), 405


if __name__ == "__main__":
    try:
        app.run(host="127.0.0.1", port=8080, debug=False)
        Timer(1, lambda: webbrowser_open("http://127.0.0.1:8080")).start()
    except Exception as e:
        print(f"[ FAIL ] Error: {e}")