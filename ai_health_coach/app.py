from flask import Flask, render_template, request, session
from config import Config
from agent import health_coach_agent

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    profile = {
        "age": int(request.form["age"]),
        "gender": request.form["gender"],
        "sleep_hours": float(request.form["sleep"]),
        "steps": int(request.form["steps"]),
        "stress_level": request.form["stress"],
        "uneasiness": request.form["uneasiness"],
        "health_goal": request.form["goal"]
    }

    summary = health_coach_agent(profile)

    return render_template("result.html", summary=summary)

# Chatbot version
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if "messages" not in session:
        session["messages"] = []

    if request.method == "POST":
        user_input = request.form["message"]
        session["messages"].append({"role": "user", "content": user_input})

        profile = {
            "age": 25,
            "gender": "Not Specified",
            "sleep_hours": 7,
            "steps": 5000,
            "stress_level": "Medium",
            "uneasiness": "None",
            "health_goal": "General Fitness"
        }

        response = health_coach_agent(profile)
        session["messages"].append({"role": "assistant", "content": response})

    return render_template("chat.html", messages=session["messages"])

if __name__ == "__main__":
    app.run(debug=True)