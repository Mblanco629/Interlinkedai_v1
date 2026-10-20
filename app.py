import os

from flask import Flask, render_template


app = Flask(__name__, template_folder="static/templates")
# port = int(os.environ.get("PORT", "5000"))


@app.get("/")
def home():
    return render_template("interlinkedai.html")


#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=port, debug=False)
