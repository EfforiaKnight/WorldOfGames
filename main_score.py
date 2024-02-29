import os
from pathlib import Path

from flask import Flask, render_template

from app.utils import SCORES_FILE_NAME

app = Flask(__name__, template_folder="templates")


@app.route("/")
def score_server():
    try:
        score = Path(SCORES_FILE_NAME).read_text()
        html = render_template("success.html", score=score)
    except Exception as e:
        html = render_template("error.html", error=str(e))

    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("FLASK_RUN_PORT", 5000))
