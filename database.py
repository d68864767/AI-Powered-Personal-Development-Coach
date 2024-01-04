```python
from pymongo import MongoClient
from user_model import User
from goal_model import Goal
from interaction_model import Interaction

class Database:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['personal_development_coach']

    def save_user(self, user):
        users = self.db.users
        user_id = users.insert_one(user.to_dict()).inserted_id
        return user_id

    def get_user(self, id):
        users = self.db.users
        user_data = users.find_one({'_id': id})
        if user_data:
            return User(user_data)
        else:
            return None

    def save_goal(self, goal):
        goals = self.db.goals
        goal_id = goals.insert_one(goal.to_dict()).inserted_id
        return goal_id

    def get_goal(self, id):
        goals = self.db.goals
        goal_data = goals.find_one({'_id': id})
        if goal_data:
            return Goal(goal_data)
        else:
            return None

    def save_interaction(self, interaction):
        interactions = self.db.interactions
        interaction_id = interactions.insert_one(interaction.to_dict()).inserted_id
        return interaction_id

    def get_interaction(self, id):
        interactions = self.db.interactions
        interaction_data = interactions.find_one({'_id': id})
        if interaction_data:
            return Interaction(interaction_data)
        else:
            return None
```
