from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# This block is useful for local dev; Vercel ignores it.
if __name__ == "__main__":
    app.run(debug=True)
