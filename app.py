from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    game_over = False

    if request.method == "POST":
        try:
            user_guess = int(request.form["guess"])
        except ValueError:
            message = "⚠️ Please enter a valid number."
            return render_template("index.html", message=message)

        secret_number = int(request.form["secret_number"])
        current_try = int(request.form["current_try"]) + 1
        max_try = 3

        if user_guess == secret_number:
            message = "✅ You've guessed the number!"
            game_over = True
        elif current_try == max_try:
            message = f"😓 You're out of guesses. The number was {secret_number}."
            game_over = True
        elif user_guess < secret_number:
            message = f"❌ Too low. Attempts left: {max_try - current_try}"
        else:
            message = f"❌ Too high. Attempts left: {max_try - current_try}"

        return render_template("index.html", message=message,
                               secret_number=secret_number,
                               current_try=current_try,
                               game_over=game_over)

    # GET request (new game)
    return render_template("index.html",
                           secret_number=random.randint(1, 100),
                           current_try=0,
                           game_over=False)
