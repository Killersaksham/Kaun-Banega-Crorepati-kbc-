from flask import Flask, render_template, jsonify
import os

app = Flask(__name__, template_folder='templates', static_folder='')

# Game data
questions = [
    "What is the Heisenberg Uncertainty Principle related to?",
    "Which number is known as the Hardy-Ramanujan number?",
    "What is the capital of the country with the world's northernmost permanent settlement?",
    "Which element has the highest melting point?",
    "Who formulated the laws of planetary motion?",
    "Which Indian physicist won the Nobel Prize in 1930 for Physics?",
    "What does the acronym 'LASER' stand for?"
]


options = [
    ["Quantum Mechanics", "Relativity", "Thermodynamics", "Electromagnetism"],
    ["1729", "1089", "2718", "3141"],
    ["Oslo", "Reykjavik", "Longyearbyen", "Tromsø"],
    ["Tungsten", "Carbon", "Osmium", "Iron"],
    ["Isaac Newton", "Galileo Galilei", "Johannes Kepler", "Tycho Brahe"],
    ["Homi Bhabha", "Satyendra Nath Bose", "C. V. Raman", "Venkatraman Ramakrishnan"],
    ["Light Amplification by Stimulated Emission of Radiation", "Light Absorption by Stimulated Emission of Rays", "Linear Amplification by Stimulated Energy Radiation", "Luminous Acceleration by Static Electromagnetic Rays"]
]

correct_answers = [
    "Quantum Mechanics",
    "1729",
    "Longyearbyen",
    "Tungsten",
    "Johannes Kepler",
    "C. V. Raman",
    "Light Amplification by Stimulated Emission of Radiation"
]


phone_friend_suggestions = [
    "It's related to Quantum Mechanics, I'm sure.",
    "Definitely 1729 — Ramanujan's famous number!",
    "Pretty sure it’s Longyearbyen in Norway.",
    "Tungsten has the highest melting point.",
    "Kepler gave the laws of planetary motion.",
    "That’s C. V. Raman — Nobel Laureate 1930.",
    "LASER stands for Light Amplification by Stimulated Emission of Radiation."
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
