from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Citizen, Feedback
from analysis import analyze_feedback
import config

app = Flask(__name__)
CORS(app)
app.config.from_object(config)
db.init_app(app)
# Route to handle feedback submission
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    name = data['name']
    email = data['email']
    text = data['feedback_text']

    # Create new citizen entry
    citizen = Citizen(name=name, email=email)
    db.session.add(citizen)
    db.session.flush()  # So we can use citizen.citizen_id

    # Analyze feedback text using NLP
    sentiment, category, urgency = analyze_feedback(text)

    # Store feedback with analysis
    feedback = Feedback(
        citizen_id=citizen.citizen_id,
        feedback_text=text,
        sentiment=sentiment,
        category=category,
        urgency_level=urgency
    )
    db.session.add(feedback)
    db.session.commit()

    return jsonify({
        "message": "Feedback submitted successfully",
        "sentiment": sentiment,
        "category": category,
        "urgency": urgency
    })

# Start the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensures tables are created at startup
    app.run(debug=True, use_reloader=False)

