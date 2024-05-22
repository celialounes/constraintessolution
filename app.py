from flask import Flask, render_template, request, redirect, url_for
from csp import generate_timetable

app = Flask(__name__)

# Example storage for anomalies and solutions
anomalies = {}
constraints = {
    "Maximum de cours par jour pour un étudiant": "Répartir les cours sur plusieurs jours sans dépasser 3 cours par jour.",
    "Plage horaire préférée pour un professeur": "Placer les cours du professeur X dans les créneaux matinaux.",
    "Jour de congé pour un groupe": "Reprogrammer les cours du groupe Y pour d'autres jours.",
    "Cours consécutifs": "Insérer des pauses entre les cours pour éviter plus de deux cours consécutifs.",
    "Nombre maximum de créneaux par semaine pour un professeur": "Répartir les cours pour le professeur Z pour ne pas dépasser 10 créneaux par semaine.",
    "Cours obligatoires à des créneaux spécifiques": "Placer le cours A le lundi matin et ajuster les autres cours."
}

user_constraints = []

@app.route('/')
def index():
    timetable = generate_timetable(user_constraints)
    return render_template('results.html', timetable=timetable, anomalies=anomalies, constraints=constraints)

@app.route('/submit_anomaly', methods=['POST'])
def submit_anomaly():
    anomaly = request.form['anomaly']
    solution = "Solution to be determined"  # Placeholder for your logic to determine the solution
    anomalies[anomaly] = solution
    return redirect(url_for('index'))

@app.route('/submit_constraint', methods=['POST'])
def submit_constraint():
    constraint = request.form['constraint']
    user_constraints.append(constraint)
    solution = constraints.get(constraint, "Solution to be determined")  # Placeholder for your logic to determine the solution
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
