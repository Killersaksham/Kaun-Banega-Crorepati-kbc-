from flask import Flask, render_template, jsonify
import os

app = Flask(__name__, template_folder='templates', static_folder='')

# Game data
questions = [
    "Which planet is known as the Red Planet?",
    "Who developed the Python programming language?",
    "What is the capital of France?",
    "What is H2O commonly known as?",
    "Who was the first person to walk on the Moon?",
    "Which Indian cricketer is known as the 'Master Blaster'?",
    "What is the largest organ in the human body?"
]

options = [
    ["Earth", "Mars", "Jupiter", "Venus"],
    ["Guido van Rossum", "Dennis Ritchie", "James Gosling", "Linus Torvalds"],
    ["Berlin", "Madrid", "Paris", "Lisbon"],
    ["Salt", "Oxygen", "Hydrogen", "Water"],
    ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Rakesh Sharma"],
    ["Virat Kohli", "MS Dhoni", "Rahul Dravid", "Sachin Tendulkar"],
    ["Heart", "Skin", "Lungs", "Liver"]
]

correct_answers = [
    "Mars", "Guido van Rossum", "Paris", "Water",
    "Neil Armstrong", "Sachin Tendulkar", "Skin"
]

phone_friend_suggestions = [
    "I'm pretty sure it's Mars.",
    "That's definitely Guido van Rossum.",
    "Paris is the capital of France!",
    "H2O? That’s water, of course.",
    "Neil Armstrong was the first.",
    "Has to be Sachin Tendulkar.",
    "The skin is the largest organ."
]

prize_pool = ["₹1,000", "₹2,000", "₹3,000", "₹5,000", "₹10,000", "₹20,000", "₹40,000"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_question/<int:index>")
def get_question(index):
    if index < len(questions):
        return jsonify({
            "question": questions[index],
            "options": options[index],
            "answer": correct_answers[index],
            "suggestion": phone_friend_suggestions[index],
            "prize": prize_pool[index]
        })
    return jsonify({"end": True})

if __name__ == "__main__":
    app.run(debug=True)
