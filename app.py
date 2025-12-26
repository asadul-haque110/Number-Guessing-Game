from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/", methods=["GET", "POST"])
def index():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["attempts"] = 0

    message = ""

    if request.method == "POST":
        guess = int(request.form["guess"])
        session["attempts"] += 1

        if guess < session["number"]:
            message = "📉 Too Low!"
        elif guess > session["number"]:
            message = "📈 Too High!"
        else:
            message = f"🎉 Correct! Attempts: {session['attempts']}"
            session.pop("number")
            session.pop("attempts")

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
