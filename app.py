from flask import Flask, render_template, request
import re

app = Flask(__name__)

# -------- Password Strength Function --------
def check_strength(password):
    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 8:
        score += 2
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase Check
    if re.search("[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase Check
    if re.search("[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    # Number Check
    if re.search("[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    # Special Character Check
    if re.search("[!@#$%^&*]", password):
        score += 2
    else:
        suggestions.append("Add special characters")

    # Strength Level
    if score <= 2:
        strength = "Weak"
        time = "Few seconds"
    elif score <= 4:
        strength = "Medium"
        time = "Few minutes"
    elif score <= 6:
        strength = "Strong"
        time = "Few years"
    else:
        strength = "Very Strong"
        time = "Centuries"

    return strength, time, suggestions


# -------- Main Route --------
@app.route("/", methods=["GET", "POST"])
def index():
    strength = None
    time = None
    suggestions = []

    if request.method == "POST":
        password = request.form["password"]
        strength, time, suggestions = check_strength(password)

    return render_template(
        "index.html",
        strength=strength,
        time=time,
        suggestions=suggestions
    )


# -------- Run Application --------
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
