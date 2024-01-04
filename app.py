```python
from flask import Flask, request, jsonify
from database import Database
from openai_api import OpenAI_API
from user_model import User
from goal_model import Goal
from interaction_model import Interaction

app = Flask(__name__)
db = Database()
openai_api = OpenAI_API()

@app.route('/')
def index():
    return "Welcome to the AI-Powered Personal Development Coach!"

@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user = User(user_data)
    db.save_user(user)
    return jsonify(user.to_dict()), 201

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = db.get_user(id)
    return jsonify(user.to_dict()), 200

@app.route('/goal', methods=['POST'])
def create_goal():
    goal_data = request.get_json()
    goal = Goal(goal_data)
    db.save_goal(goal)
    return jsonify(goal.to_dict()), 201

@app.route('/goal/<id>', methods=['GET'])
def get_goal(id):
    goal = db.get_goal(id)
    return jsonify(goal.to_dict()), 200

@app.route('/interaction', methods=['POST'])
def create_interaction():
    interaction_data = request.get_json()
    interaction = Interaction(interaction_data)
    db.save_interaction(interaction)
    return jsonify(interaction.to_dict()), 201

@app.route('/interaction/<id>', methods=['GET'])
def get_interaction(id):
    interaction = db.get_interaction(id)
    return jsonify(interaction.to_dict()), 200

@app.route('/advice', methods=['POST'])
def get_advice():
    user_data = request.get_json()
    advice = openai_api.get_advice(user_data)
    return jsonify(advice), 200

if __name__ == '__main__':
    app.run(debug=True)
```
